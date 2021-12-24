#include <stdio.h>
#include <string.h>
#include <time.h>

unsigned char s[15];
unsigned long long int w=0,x=0,z=0;
unsigned long long int t=0;


void pp() {
  unsigned long long int x=10000000000000;
  t=0;
  for (int i=0;i<14;i++)
    if (s[i]>=0 && s[i]<=9)
      printf("%c",s[i]+'0'),t+=x*s[i],x/=10;
  fflush(stdout);
}

int checkadd () {

  int c=1;
  char v;
  char f=1;

  for(int i=13;i>=0;i--) {
    v=s[i]+c;
    c=v/10;
    s[i]=v%10;
    f=f&(s[i]!=0);
  }

  return f;
}


int f();

void wop(long long int ss) {
  sprintf(s,"%14lld",ss);
  for (int i=0;i<14;i++)
    s[i]-='0'; 

  while(1) {
    checkadd(s);
    f();
    pp();
    printf(" %lld\n",z);
  }
}
int main(int argc, char **argv) {
  wop(11111111111111);
		  
}
