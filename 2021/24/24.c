#include "24.h"

long int w=0,x=0,y=0,z=0;

void fg(int v1, int v2, int v3) {
  x=z%26;
  z/=v3;
  x+=v1;
  x=((x!=w)?1:0);

  y=25*x+1;

  z*=y;
  y=0;
  y+=w;

  y+=v2;
  y*=x;
  z+=y;
}


int f(){
  w=0;
  x=0;
  y=0;
  z=0;

  w=s[13];
  fg(14,7, 1);
  
  w=s[12];
  fg(12,4, 1);

  w=s[11];
  fg(11,8, 1);
  
  w=s[10];
  fg(0,1,26);
  
  w=s[9];
  fg(10,5,1);
  
  w=s[8];
  fg(10,14,1);
  
  w=s[7];
  fg(15,12,1);
  
  w=s[6];
  fg(0,10,26);
  
  w=s[5];
  fg(0,5,26);
  
  w=s[4];
  fg(12,7,1);
  
  w=s[3];
  fg(0,6,26);
  
  w=s[2];
  fg(0,8,26);
  
  w=s[1];
  fg(0,4,26);

  w=s[0];
  fg(0,6,26);
    return (z);
}
