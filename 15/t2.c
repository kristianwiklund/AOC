#include <stdio.h>
#include <unistd.h>
#include <string.h>
#define MAXY 41
#define MAXX 41

int spaces=0;

char data[MAXY][MAXX+1] = { 
  "#########################################",
  "#   #       #         #           #   # #",
  "# # ### # ### ### ### ### # ##### # # # #",
  "# #   # #       # #     # # #     # # # #",
  "# ### ######### # ##### ### # ##### # # #",
  "# #*# #     #   #   #       # #   # # # #",
  "# # # # ### ####### ######### # # # # # #",
  "# #     # #   #   #   #     #   #   # # #",
  "# ####### ### # # ### # # ########### # #",
  "#       #   #   # #   # #       #   #   #",
  "# ##### # ####### # ####### ##### # ### #",
  "# #   # #         #   #   #       #   # #",
  "# ### # ### ######### # # ### ##### # # #",
  "#     #   # #   #     # #   #     # # # #",
  "##### ### # # # ### # # ### ####### # # #",
  "#     #   #   #     # # # #   #     # # #",
  "# ##### ####### ####### # ### # ####### #",
  "# #   #   #     #   #   # #   # #       #",
  "# ### ### ### ### # # ### # ### # #######",
  "#       #   # #   #   #   #   # #     # #",
  "# ######### # # ####### ##### # ##### # #",
  "# #     #   # #       # #     # #     # #",
  "### ### # ### ######### # ##### # ##### #",
  "#   #   # # #   #   #   #     # # #   # #",
  "# ### ### # # ### # # # ##### # # # # # #",
  "# #       #   #   #   #     # # #   # # #",
  "# ######### ### ########### # # ##### # #",
  "# #     #   # # #     #   #   #     # # #",
  "# # ### # ### # # # ### # ##### ### # # #",
  "# # # # # #   # # # #   #     # #   #   #",
  "# # # # # ### # ### # ##### # # # ##### #",
  "# #   # #   # #   #       # # # # #     #",
  "# # ### ### # ### ####### # # ### # #####",
  "# # #   #       #   #     # # #   # #   #",
  "# # # ##### ####### # ##### # # # # # # #",
  "#   # #   # #   #   # # #   #   # # # # #",
  "##### # # ### # # ### # # ####### # ### #",
  "#   #   #     #   # #   #   #   # #   # #",
  "# # ############### ### ### # # ##### # #",
  "# #                       #   #         #",
  "#########################################"};

char newdata[MAXY][MAXX+1];

void oxygenate(int x, int y) {
  if (data[y][x] != ' ')
    return;

  newdata[y][x] = 'O';
  spaces--;
}

void tick(){

  for (int y=0;y<MAXY;y++)
    strcpy(newdata[y],data[y]);
  
  for (int y=0;y<MAXY;y++)
    for (int x=0;x<MAXX;x++) {

      if (data[y][x] == 'O') {
	oxygenate(x,y+1);
	oxygenate(x,y-1);
	oxygenate(x+1,y);
	oxygenate(x-1,y);
      }
      
    }
  for (int y=0;y<MAXY;y++)
    strcpy(data[y],newdata[y]);
  
}
  

int main(int argc, char **argv) {
  int startx = 0, starty = 0 ;
  int clock =0;
  int os = 0;
  
  for (int y=0;y<MAXY;y++) 
    for (int x=0;x<MAXX;x++) 
      if (data[y][x] == '*') {
	startx = x;
	starty = y;
    } else
	if (data[y][x] == ' ' )
	  spaces++;
  printf("Start: (%d,%d) %d empty spaces\n", startx, starty, spaces);

  data[starty][startx] = 'O';
  
  while(spaces) {
    tick();
    //for(int i=0;i<MAXY;i++)
    //  printf("%s\n",data[i]);
    clock++;
    //    sleep(1);
  }
  printf("Full, after %d ticks\n", clock);
  // 136 - too low
  // hence. 135 must also be too low
  
  //for(int i=0;i<MAXY;i++)
  //  printf("%s\n",data[i]);
  
}
