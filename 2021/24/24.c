#include "24.h"

inline void fg(int v1, int v2) {
  x=(z%26)+v1; 

  if (x!=w) {
    z=26*z+w+v2;
  }
}

inline void fg0(int v2, int v3) {
  x=(z%26); 
  z=z/v3;      

  if (x!=w) {
    z=26*z+w+v2;
  }
}

inline void fg0_26(int v2) {
  x=z%26; 
  z=z/26;      

  if (x!=w) {
    z=26*z+w+v2;
  }
}


int f(){
  w=0;
  x=0;
  z=0;

  w=s[0];
  fg(14,7);
  
  w=s[1];
  fg(12,4);

  w=s[2];
  fg(11,8);
  
  w=s[3];
  fg0_26(1);
  
  w=s[4];
  fg(10,5);
  
  w=s[5];
  fg(10,14);
  
  w=s[6];
  fg(15,12);
  
  w=s[7];
  fg0_26(10);
  
  w=s[8];
  fg0_26(5);
  
  w=s[9];
  fg(12,7);
  
  w=s[10];
  fg0_26(6);
  
  w=s[11];
  fg0_26(8); 
  
  w=s[12];    
  fg0_26(4); 

  w=s[13]; // 0 if w = z %% 26
  printf("z=%lld z mod 26=%lld w=%lld / ",z, z%26,w);
  fg0_26(6);
    return (z);
}
