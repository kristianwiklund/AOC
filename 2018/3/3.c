#include <stdio.h>
#include <string.h>
int **allocmax(char *fn) {
  FILE *f;
  char buf[100];
  int maxx=0,maxy=0;
  int **m;
  char *s;
  int x,y,xs,ys;
  char *b;
  
  f = fopen("input.txt","r");

  while(fgets(buf, 100, f)) {
    s = strtok_r(buf,"@,:x",&b);
      s = strtok_r(0, "@,:x",&b);
      x = atoi(s);
      s = strtok_r(0, "@,:x",&b);
      y = atoi(s);
      s = strtok_r(0, "@,:x",&b);
      xs = atoi(s);
      s = strtok_r(0,"@:,x",&b);
      ys = atoi(s);
      maxx = (x+xs)>maxx?x+xs:maxx;
      maxy = (y+ys)>maxy?y+ys:maxy;
    }
    
  fclose(f);

  printf("-->%d,%d<<-\n",maxx,maxy);

  m = (int **)calloc(maxx , sizeof(int*));
  for(int i = 0; i < maxx; i++) m[i] = (int *)calloc(maxy , sizeof(int));


    return m;
}

int fillerup(char *fn, int **m) {
  FILE *f;
  char buf[100];
  int maxx=0,maxy=0;
  char *s;
  int x,y,xs,ys;
  char *b;
  int cnt=0;
  
  f = fopen("input.txt","r");

  while(fgets(buf, 100, f)) {
    s = strtok_r(buf,"@,:x",&b);
    s = strtok_r(0, "@,:x",&b);
    x = atoi(s);
    s = strtok_r(0, "@,:x",&b);
    y = atoi(s);
    s = strtok_r(0, "@,:x",&b);
    xs = atoi(s);
    s = strtok_r(0,"@:,x",&b);
    ys = atoi(s);
     
    maxx = (x+xs)>maxx?x+xs:maxx;
    maxy = (y+ys)>maxy?y+ys:maxy;

      for(int i=x;i<x+xs;i++)
	for(int j=y;j<y+ys;j++)
	  m[i][j]++;
    }
    
  fclose(f);

  printf("-->%d,%d<<-\n",maxx,maxy);

  for (int i=0;i<maxx;i++)
    for (int j=0;j<maxy;j++)
      cnt+=(m[i][j]>1);
  
  return cnt;
}


void main() {

  int **m = allocmax("input.txt");
  
  printf("%d\n",fillerup("input.txt",m));
}
