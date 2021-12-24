#include <stdio.h>
#include <string.h>
#include <time.h>

char s[15];

int checkadd () {

  int i=0;
  int c=1;
  char v;
  char f=1;
  
  while(i<14) {
    v=s[i]+c;
    c=v/10;
    s[i]=v%10;
    f=f&(s[i]!=0);
    i++;

  }
  return f;
}

void pp() {

  for (int i=13;i>=0;i--)
    printf("%c",s[i]+'0');
  fflush(stdout);
}

int f();

int main(int argc, char **argv) {
  int z,cnt=0;
  sprintf(s,"%ld",11111111111111);
  for (int i=0;i<14;i++)
    s[i]-='0';
  
  while(1) {

    if (checkadd(s)) {
      z=f();
      if (!z)
	printf("%s %d\n", s, z);

      cnt++;
      if (!(cnt%10000000)) {
        pp();
	printf(" %d\n",z);
      }
    }
  }

}
