#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "input.h"

int main(int argc, char **argv) {

  int *a = calloc(strlen(ap)*10,sizeof(int));
  int c=0;
  int ac=0;
  int x;
  long int cksum;
  int i,j;

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

  i=0;
  j=strlen(ap)*10-1;

  
  while(i<j) {

    // don't move anything already in place

    if (a[i]!=-1) {
      i++;
      continue;
    }

    // free space. move stuff here

    if (a[j]==-1) {
      j--;
      continue;
    }

    //printf("move %d (%d) to %d\n", j,a[j],i);
    a[i++]=a[j];
    a[j--]=-1;
    
  }

  printf("done\n");

  cksum=0;
  for(i=0;i<strlen(ap)*10;i++)
    if (a[i]>-1)
      cksum+=i*a[i];

  printf("cksum: %ld\n", cksum);
}
