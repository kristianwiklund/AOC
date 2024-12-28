A= 66171486
B= 0
C= 0
P= "2416754614550330"
def run(A):
  B= A % 8
  B=B ^ 6
  B=A // (2** B )
  B=B^C
  B=B ^ 4
  P= B  % 8
  A=A // (2** 3 )
  # goto  0
  return (A,P)

def d(A):
 S=""
 while True:
  (A,P) = run (A)
  S+=str(P)
  if not A:
    break
 return(S)

c=35500000000000
while True:
 s = d(c)
 if s==P:
   print(c,P)
   break
 c+=1
 if not c%100000:
   print(c,s,len(s))
 if len(s)>len(P):
  print(s,P)
