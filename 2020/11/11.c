#include "input.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void *matrix[2];

int bopp(char **M, int y, int x) {

  if((y<0) || (x<0) || (x==SX) || (y==SY))
    return 0;

  return ((M[y][x]=='#')?1:0);
  
}

int chonk(char **M, int y, int x) {

  int s=0;
  
  s+=bopp(M, y-1, x);
  s+=bopp(M, y+1, x);
  s+=bopp(M, y, x-1);
  s+=bopp(M, y, x+1);

  s+=bopp(M, y-1, x-1);
  s+=bopp(M, y+1, x-1);
  s+=bopp(M, y+1, x+1);  
  s+=bopp(M, y-1, x+1);

  return s;
  
}

int bapp(int what) {

char **M = (char **)matrix[what];
char **N = (char **)matrix[1-what];
 int t;
 int f=0;
 
  for(int y=0;y<SY;y++) {
    for(int x=0;x<SX;x++) {

      N[y][x] = M[y][x];

      t = chonk(M,y,x);
      
      if(M[y][x] == 'L') {
	if(t == 0) {
	  N[y][x] = '#';
	  f++;
	}
      }
      
      if(M[y][x] == '#') {
	if(t >= 4) {
	  N[y][x] = 'L';
	  f++;
	}
      } 
      
      //      printf("%c/%c(%d) ",M[y][x],N[y][x],t);
      //printf("%c",N[y][x]);

    }
    //puts("");
  }
  return(f);
}
  

int main() {
  char **b,**a,**c;
  int p, which=0;
  c= (void *)input;
 a = calloc(sizeof(char *), SY);
 b = calloc(sizeof(char *), SY);
 
 for (int y=0;y<SY;y++) {
   b[y] = strdup(c[y]);
   a[y] = strdup(c[y]);
 }
 matrix[1] = (void *)b;
 matrix[0] = (void *)a;

   do {
     p = bapp(which);
     
     //     puts("------");
     //     printf("%d: %d\n", which, p);
     which=1-which;
   } while(p>0);

   //once more, with feeling
   p = bapp(which);
   which = 1 - which;
   
   p=0;
   c = (char **)matrix[which];
   
  for(int y=0;y<SY;y++) {
    for(int x=0;x<SX;x++) {
      
      if (c[y][x]=='#')
	p++;
      //      printf("%c",c[y][x]);
    }
    //puts("");
  }
  
      printf("%d occupied seats\n", p);
}

