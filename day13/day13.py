def g(X,Y):
 for x,y in zip(eval(X), eval(Y)):
  if type(x)==type(y)==int:
   if x==y:continue
   return -1 if x<y else 1
  if type(x)==list!=type(y):y=[y]
  if type(x)!=list==type(y):x=[x]
  r=g(str(x),str(y))
  if r!=0:return r
 return -1 if len(X)<len(Y) else 1 if len(X)>len(Y) else 0
n,a,b=0,1,2
for i,(l,r)in enumerate(map(str.split,open('day13/input.txt').read().split('\n\n'))):
 if g(l,r)!=1:n+=i+1
 a+=(g(l,'[[2]]')==-1)+(g(r,'[[2]]')==-1)
 b+=(g(l,'[[6]]')==-1)+(g(r,'[[6]]')==-1)
print(n,a*b)