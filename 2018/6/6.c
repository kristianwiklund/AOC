#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include "6.h"

void printstats() {

  int cnt[NRCOORD+1];

  for (int i=0;i<NRCOORD+1;i++)
    cnt[i]=0;
  
  for (int y=0;y<MAXY;y++)
    for (int x=0;x<MAXX;x++)
      if (data[y][x] != '.')
	cnt[data[y][x]-48]++;

  for (int i=0;i<NRCOORD+1;i++)
    printf("%d: %d\n", i, cnt[i]);
}




void calculon(int x, int y) {
  
  int min=INT_MAX, dist;
  data[y][x]=0;
  
  for (int i = 0;i<NRCOORD;i++) {
    dist = abs(x-cx[i])+abs(y-cy[i]);

    if (dist<min) {
      min=dist;
      data[y][x]=48+i;
    }  else {
      if (dist==min) { // more than one on the same distance that is the min distance
	data[y][x] = '.';
      }
    }
  }
      
}

int main(int argc, char **argv) {
  int startx = 0, starty = 0 ;
  int clock =0;
  int os = 0;
  int x;
  setup();
  
  for (int y=0;y<MAXY;y++) {
    for (x=0;x<MAXX;x++) {
      calculon(x,y);
    }
  }

  //  printfield();
  printstats();
  

  
}
