#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include "6.h"



int spaces=0;


void printfield() {

  for (int x=0;x<MAXX+2;x++)
    printf("-");
  puts("");
  
  for (int y=0;y<MAXY;y++)
    printf("|%s|\n",(data[y]));
  
  for (int x=0;x<MAXX+2;x++)
    printf("-");
  puts("");
}

void grow(int x, int y, char c) {

  if(x<0 || x>=MAXX || y<0 || y>=MAXY)
    return;

  if (data[y][x] == ' ') {
    if ((newdata[y][x] != ' ') )
      newdata[y][x] = '.';
    else {
      newdata[y][x] = c;
      spaces--;
    }
  }
}

void tick(){
  
  for (int y=0;y<MAXY;y++)
    strcpy(newdata[y],data[y]);
  
  for (int y=0;y<MAXY;y++)
    for (int x=0;x<MAXX;x++) {

      if ((data[y][x] != ' ')) { // && (data[y][x] != '.')) {
	grow(x,y+1,data[y][x]);
	grow(x,y-1,data[y][x]);
	grow(x+1,y,data[y][x]);
	grow(x-1,y,data[y][x]);
      }
      
    }
  for (int y=0;y<MAXY;y++)
    strcpy(data[y],newdata[y]);
  
}
  

int main(int argc, char **argv) {
  int startx = 0, starty = 0 ;
  int clock =0;
  int os = 0;
  int x;
  
  for (int y=0;y<MAXY;y++) {
    for (x=0;x<MAXX;x++) {
      data[y][x]= ' ';
    }
    data[y][x]= 0;
  }

  setup();
  printfield();
  
  
  for (int y=0;y<MAXY;y++) 
    for (int x=0;x<MAXX;x++) 
      if (data[y][x] == ' ' )
	spaces++;


  while(spaces) {
    tick();
    printfield();
    sleep(1);
    //for(int i=0;i<MAXY;i++)
    //  printf("%s\n",data[i]);
    clock++;
    //    sleep(1);
  }
  // 136 - too low
  // hence. 135 must also be too low
  
  //for(int i=0;i<MAXY;i++)
  //  printf("%s\n",data[i]);
  
}
