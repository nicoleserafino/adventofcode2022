d=[x.strip()for x in open('day08/input.txt').readlines()]
p1,p2=99+98+98+97,0
dirs=[(-1,0),(1,0),(0,-1),(0,1)]
for i in range(1,len(d)-1):
 for j in range(1,len(d)-1):
  for k in dirs:
   x,y = i+k[0],j+k[1]
   while 0<x<len(d)-1>y>0 and d[i][j]>d[x][y]:
    x,y=x+k[0],y+k[1]
   if d[i][j]>d[x][y]and(x==0 or x==len(d)-1 or y==0 or y==len(d)-1):
    p1+=1
    break
for i in range(1,len(d)-1):
 for j in range(1, len(d)-1):
  s=1
  for k in dirs:
   c=0
   x,y=i+k[0],j+k[1]
   while 0<=x<=len(d)-1>=y>=0:
    c+=1
    if d[i][j]<=d[x][y]:
     break
    x,y=x+k[0],y+k[1]
   s*=c
  p2=max(p2,s)
print(p1,p2)