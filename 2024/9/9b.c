#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "input.h"

int main(int argc, char **argv) {

  int *a = calloc(strlen(ap)*10,sizeof(int));
  int *b = calloc(strlen(ap)*10,sizeof(int));
  int c=0;
  int ac=0;
  int x,y;
  long long int cksum;
  int i,j;
  int moved=0;
  
  printf("strlen(ap)=%ld\n",strlen(ap));
  
  memset(a, -1, sizeof(int)*10*strlen(ap)); 

  for (i=0;i<strlen(ap)/2;i++) {
    
    x = ap[2*i]-'0';
    for(j=0;j<x;j++)
      a[ac++]=c;

    if(x==0)
      printf("zero length file: %d\n", c);

    c++;

    x = ap[2*i+1]-'0';
    for(j=0;j<x;j++)
      a[ac++]=-1;  
  }


  memcpy(b,a, sizeof(int)*10*strlen(ap)); 
  
  // attempt to move exactly once -> meaning that we set the pointer at the start,
  // we do not reset it at each loop
  
  j=strlen(ap)*10-1;

  
  do {
    int fn, fp;
    
    // find a block to move

    // chomp the empty blocks at the end of the storage area
    for (;a[j]==-1;j--);
    
    fn = a[j];
    fp = j;
    
    // we have found something at the end
    printf("block %d: found file %d which is", fp, fn);

    for(;a[j]==fn;j--);
    
    printf(" %d blocks long\n", fp-j);

    // now find an empty block >= the size of the identified file

    i = 0;
    
    do {
      
      for(;b[i]!=-1;i++)
	if (i>=j)
	  goto hoppsan;
      
      for(x=i;b[x]==-1;x++)
	if(x>j)
	  goto hoppsan;

      if((x-i)>=(fp-j)) {
	printf("...moving file %d to %d\n", fn, i);
        for(y=0;y<fp-j;y++)
	  b[i+y]=fn;
	for(x=j+1;x<=fp;x++) {
	  a[x]=-1;
	  b[x]=-1;
	}

	goto hoppsan;
      }

      i++;
    } while(i<j);
    

    
  hoppsan:
    printf("Unable to move file %d. Moving on...\n", fn);
    
  } while(j>=0);
  


  if (strlen(ap)<80) {
    for(y=0;y<strlen(ap)*10;y++) 
      printf("%c",b[y]>-1?b[y]+'0':'.'); 
    printf("\n"); 
  }
    
  cksum=0;
  for(i=0;i<strlen(ap)*10;i++)
    if (b[i]>-1)
      cksum+=i*b[i];

  printf("cksum: %lld\n", cksum);
}
