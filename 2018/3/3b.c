#include <stdio.h>
#include <string.h>

int **m,*c;

int **allocmax(char *fn) {
  FILE *f;
  char buf[100];
  int maxx=0,maxy=0,maxid=0;
  char *s;
  int x,y,xs,ys,id;
  char *b;

  f = fopen("input.txt","r");

  while(fgets(buf, 100, f)) {
    s = strtok_r(buf,"@,:x",&b);
    id = atoi(s+1);
    maxid=(id>maxid)?id:maxid;
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
  c = calloc(maxid,sizeof(int));
}

int fillerup(char *fn) {
  FILE *f;
  char buf[100];
  int maxx=0,maxy=0,maxid=0;
  char *s;
  int x,y,xs,ys;
  char *b;
  int cnt=0,id;
  
  f = fopen("input.txt","r");

  while(fgets(buf, 100, f)) {
    s = strtok_r(buf,"@,:x",&b);
    id = atoi(s+1);
    maxid=(id>maxid)?id:maxid;
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
	for(int j=y;j<y+ys;j++) {
	  if(m[i][j]) {
	    c[m[i][j]] = -1;
	    c[id]=-1;
	  }
	  m[i][j] = id;
	}

  }
    
  fclose(f);

  printf("-->%d,%d<<-\n",maxx,maxy);

  for (int i=1;i<maxid;i++)
    if(!c[i])
    return(i);
  
  return -1;
}


void main() {

  int **m = allocmax("input.txt");
  
  printf("%d\n",fillerup("input.txt"));
}
