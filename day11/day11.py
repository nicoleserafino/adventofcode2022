d=[x for x in open("day11/input.txt").read().splitlines()]
o=[(d[x][23:])for x in range(2,len(d),7)]
t=[int(d[x][21:])for x in range(3,len(d),7)]
c=[[int(d[x][29:]),int(d[x+1][30:])]for x in range(4,len(d),7)]
m=eval('*'.join(str(x)for x in t))
for p in [20, 10000]:
 s=[[[int(x)for x in(d[y][18:]).split(", ")]for y in range(1,len(d),7)]][0]
 n=[0]*len(t)
 for _ in range(p):
  for i in range(len(n)):
   for j in range(0,len(s[i])):
    x=s[i][j]
    if o[i]=="* old":x*=x
    elif o[i][:2]in["* ","+ "]:x=eval(str(x)+o[i])
    x=x//3 if p==20 else x%m
    if x%t[i]==0:s[c[i][0]].append(x)
    else:s[c[i][1]].append(x)  
    n[i]+=1
   s[i]=[]
 print(max(n)*sorted(n)[-2])