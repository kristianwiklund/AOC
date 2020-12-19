
%%
input: | t0 input;
t0: t4 t1 t5 '\n' {printf("1\n");}
t1: t2 t3 | t3 t2;
t2: t4 t4 | t5 t5;
t3: t4 t5 | t5 t4;
t4: 'a';
t5: 'b';

%%
int main() {
  while(1) yyparse();
}

yyerror (s)  /* Called by yyparse on error */
     char *s;
{
  printf ("%s\n", s);
}
#include <ctype.h>
#include <stdio.h>

yylex ()
{
  int c;

  /* skip white space  */
  while ((c = getchar ()) == ' ' || c == '\t')  
    ;
  if (c == EOF)                            
    exit(0);
  /* return single chars */
  //    printf("%c",c);

  return c;                                
}

