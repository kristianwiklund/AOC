#include "input2.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// insert x somewhere in the list
void insert(long int x, int position) {

  int len;
  
  if (position==0) {
    //    //printf("insert memmove\n");
    memmove(bop+1,bop,(INPUT)*sizeof(long int));
    *bop=x;
    return;
  }

  len=1+INPUT-position;
  
  memmove(bop+position+1,bop+position,len*sizeof(long int));
  *(bop+position)=x;    
}

// remove whatever is at position and compress the list
// will leave junk at the end
void kill(int position) {
  int len=INPUT-position+1;
  //  //printf("memmove\n");
  //  pp();
  memmove(bop+position,bop+position+1,len*sizeof(long int));
  //pp();
    
}

// move the int at position old to position new
// no error checking whatsoever
void move(int old, int new) {
  long int t;

  t = bop[old];

  kill(old);

  insert(t, new);

}

long int strip(long int where) {
  long int w=where;
  
  while(w<-OFFSET)
    w+=OFFSET;
  
  while(w>OFFSET)
    w-=OFFSET;
  
  //  printf("Offset is %ld. Converted %ld to %ld\n",OFFSET,where,w);
  return w;
}

int modulo(int x,int N){
  return (x % N + N) %N;
}


void shoffle(long int what) {
  ////printf("Shuffle %ld\n",what);
  
  long int pos=-1, newpos;
  long where=what;
  
  if (what==0)
    return;

  for (int i=0;i<INPUT;i++) {
    if (bop[i]==what) {
      pos=i;
      break;
    }
  }
  
  if (pos<0) // fail
    return;

  where=strip(where);

  //  //printf("%ld was decoded to %ld\n",what,where);

  newpos=(pos+where);
  printf("Newpos %ld\n",newpos);
    
  //while(newpos<0) { */
  //   newpos = newpos+INPUT-1; */
  // } */

    
  /* printf("Newpos negcorr %ld\n",newpos); */

  /* while(newpos>=INPUT) { */
  /*   newpos = newpos-INPUT+1; */
  /* } */

  /* printf("Newpos poscorr %ld\n",newpos); */
   
  newpos = modulo(newpos, (INPUT-1));
  printf("Newpos mod %ld %ld\n",INPUT-1,newpos);


  if (newpos<0 || newpos>=INPUT) {
    //printf("Danger will robinson %ld\n",newpos);
    exit(0);
  }
 
  //  //printf("Move %ld from  %ld to %ld\n", what, pos, newpos);
  if (newpos==0 && what<0) {
    //  //printf("We fell off the tape to the left\n");
    newpos=INPUT-1;
  }

  if (newpos>=(INPUT-1) && what>0) {
    ////printf("We fell off the tape to the right\n");
    newpos=0;
  }

  move(pos, newpos);

}

void pp() {
  if (INPUT>10)
    return;
  
  puts("----");
  for (int i=0;i<INPUT;i++) {
    printf("%ld,",bop[i]);
  }
  puts("");
  puts("----");
}

int t1() {
  //pp();
  shoffle(-9);
  //pp();
  exit(0);
}


int main() {
  int zero;
  int i,cnt,a,b,c;
  
  long int sl[INPUT];
  memmove(sl,bop,(INPUT)*sizeof(long int));

  printf("The input is %ld words long\n",INPUT);
    pp();
    
  for (int j=0;j<10;j++) {
    printf("Shuffle round %d\n",j);
  for (int i=0;i<INPUT;i++) {
    printf("%ld\n",sl[i]);
    shoffle(sl[i]);
    pp();
  }
  }
  pp();
  zero=-1;
  i=0;
  cnt=0;
  puts("Seeking answers");
  
  while(1) {
    if (!bop[i] && zero<0) {
      zero=i;
      puts("Found zero");
    }
    
    if (zero>-1) {
      if(cnt==1000)
	a=bop[i];
      if(cnt==2000)
	b=bop[i];
      if(cnt==3000) {
	c=bop[i];
	break;
      }
      cnt++;
    }

    i++;
    if (i==INPUT)
      i=0;
  }

  //printf("abc %ld %ld %ld = %ld\n",a,b,c,a+b+c);
  printf("%ld %ld %ld = %ld (8372)\n",strip(bop[(zero+1000)%INPUT]),strip(bop[(zero+2000)%INPUT]),strip(bop[(zero+3000)%INPUT]),strip(bop[(zero+1000)%INPUT])+strip(bop[(zero+2000)%INPUT])+strip(bop[(zero+3000)%INPUT]));
  //  pp();
  
}






