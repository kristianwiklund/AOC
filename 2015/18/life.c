#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "input.h"

void *matrix[2];

int check(char **M, int y, int x) {

  if((y<0) || (x<0) || (x>=XMAX) || (y>=YMAX))
    return 0;

  return ((M[y][x]=='#')?1:0);
  
}


int test(char **M, int x, int y) {

  int s=0;

  // this counts all neighbors around x,y
  s+=check(M, y-1, x);
  s+=check(M, y+1, x);
  s+=check(M, y, x-1);
  s+=check(M, y, x+1);
  
  s+=check(M, y-1, x-1);
  s+=check(M, y+1, x-1);
  s+=check(M, y+1, x+1);  
  s+=check(M, y-1, x+1);

  // this is the test

  if(M[y][x]=='#' && (s==2 || s==3))
    return 1;

  if(M[y][x]=='.' && s==3)
    return 1;
  
  return 0;
}

void print(char **M) {

  for(int y=0;y<YMAX;y++) {
    puts(M[y]);
  }
}

void run(int which) {

  // set up active frame buffer and the next one
  char **M = (char **)matrix[which];
  char **N = (char **)matrix[1-which];
  
  for(int y=0;y<YMAX;y++) {

    for(int x=0;x<XMAX;x++) {

      if(test(M,x,y))
	N[y][x] = '#';
      else
	N[y][x] = '.';       
    }
    
  }

}

int main() {
  
  char **b,**a,**c;
  int p, which=0;
  int i;
  
  // copy the input data to be able to do simultaneous simulation
  
  c= (void *)input;
  a = calloc(sizeof(char *), YMAX);
  b = calloc(sizeof(char *), YMAX);
  
  for (int y=0;y<YMAX;y++) {
    b[y] = strdup(c[y]);
    a[y] = strdup(c[y]);
  }
  matrix[1] = (void *)b;
  matrix[0] = (void *)a;

  for(i=0;i<4;i++)
    run(i%2);
  print(matrix[i%2]);
  
  
}

