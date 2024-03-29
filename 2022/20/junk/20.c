#include "input.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// insert x somewhere in the list
void insert(int x, int position) {

  int len;
  
  if (position==0) {
    //    //printf("insert memmove\n");
    memmove(bop+1,bop,INPUT*sizeof(long int));
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
  //  //printf("Kill old %ld\n",old);
  kill(old);
  //pp();
  //  //printf("Insert new %ld\n",new);
  insert(t, new);
  //pp();

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

  while(where<-OFFSET)
    where+=OFFSET;
  
  while(where>OFFSET)
    where-=OFFSET;

  //  //printf("%ld was decoded to %ld\n",what,where);

  newpos=(pos+where);
  //  //printf("Newpos %ld\n",newpos);
  while(newpos<0) {
    newpos = newpos+INPUT-1;
  }
  //  //printf("Newpos negcorr %ld\n",newpos);
  newpos = newpos % (INPUT-1);
  //  //printf("Newpos mod %ld %ld\n",INPUT-1,newpos);


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

long int strip(long int where) {
    while(where<-OFFSET)
    where+=OFFSET;
  
  while(where>OFFSET)
    where-=OFFSET;

  return where;
}

void shuffle(long int what) {

  int pos;
  long int where=what;
  
  if(INPUT<10)
    //printf("shuffle %ld\n",what);
  
  if (what==0)
    return;

  for (int i=0;i<INPUT;i++) {
    if (bop[i]==what) {
      pos=i;
      break;
    }
  }
  if (pos<0) // fail
    exit(-1);

  where=strip(where);

  //  //printf("%ld was decoded to %ld\n",what,where);


  
  if (what>0) {
    for(int i=0;i<what;i++) {

      if (pos==INPUT-1) {
	int t=bop[INPUT-1];
	insert(1,t);
	pos=2;
	continue;
      }
      if((pos+1)>=INPUT-1) {
	//	//printf("move from %ld to 0\n",pos);
	move(pos,0);
	//pp();
      }
      else {
	////printf("move from %ld to %ld\n",pos,pos+1);
	move(pos,pos+1);
	//pp();
      }
      pos++;
      if (pos==INPUT-1)
	pos=0;
    }
    return;
  }

  if (what<0) {
    for(int i=0;i<-what;i++) {
      if (pos==0) {
	int t=bop[0];
	if(INPUT<10)
	  //printf("0 to %ld\n",INPUT-2);
	kill(0);
	bop[INPUT-1]=bop[INPUT-2];
	bop[INPUT-2]=t;
	pos=INPUT-2;
	continue;
      }
      else
	{
	  if(INPUT<10)
	    //printf("%ld pos-1 %ld %ld\n",pos,pos-1,INPUT-1);
	  if ((pos-1)==0)
	    move(pos,INPUT-1);
	  else
	    move(pos,pos-1);
	}
      pos--;
      if(pos==0)
	pos=INPUT-1;
    }
  
  }
}


void pp() {
  if (INPUT>10)
    return;
  
  puts("----");
  for (int i=0;i<INPUT;i++) {
    //printf("%ld,",bop[i]);
  }
  puts("");
  puts("----");
}

int t1() {
  //pp();
  shuffle(-9);
  //pp();
  exit(0);
}


int main() {
  int zero;
  int i,cnt,a,b,c;
  
  long int sl[INPUT];
  memmove(sl,bop,INPUT*sizeof(long int));

  //printf("The input is %ld words long\n",INPUT);
  pp();
  for (int i=0;i<INPUT;i++) {
    //    //printf("%ld\n",sl[i]);
    shoffle(sl[i]);
    pp();
  }
  //pp();
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






