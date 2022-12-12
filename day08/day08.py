d=[x.strip()for x in open('day08/input.txt').readlines()]
r,v=99+98+98+97,0
m=[(-1,0),(1,0),(0,-1),(0,1)]
for p in [0,1]:
 for i in range(1,len(d)-1):
  for j in range(1,len(d)-1):
   s=1
   for k in m:
    c,x,y=0,i+k[0],j+k[1]
    while 0<x<len(d)-1>y>0 and d[i][j]>d[x][y]and p==0:x,y=x+k[0],y+k[1]
    if d[i][j]>d[x][y]and(x==0 or x==len(d)-1 or y==0 or y==len(d)-1)and p==0:r+=1;break
    while 0<=x<=len(d)-1>=y>=0<p:
     c+=1
     if d[i][j]<=d[x][y]:break
     x,y=x+k[0],y+k[1]
    s*=c
   v=max(v,s)
print(r,v)