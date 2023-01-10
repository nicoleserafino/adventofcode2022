g=[*open('day24/input.txt')]
h,w=len(g)-2,len(g[0].strip())-2
f=lambda p:complex(p.real%w, p.imag%h)
d={'x':0,'<':-1,'>':+1,'^':-1j,'v':+1j}
b={i:{complex(x,y)for x in range(w)for y in range(h)if g[y+1][x+1]==i} for i in d}
x,y=complex(0,-1),complex(w-1,h)
k,m,r=[x],0,0
while k:
 b={i:{f(p+d[i])for p in b[i]}for i in d}
 c={p+d[i]for p in k for i in d}
 k,m=[],m+1
 for p in c:
  if(r, p)in ((0,y),(1,x),(2,y)):
   if r==0:print(m)
   if r==2:print(m);exit()
   k,r=[p],r+1;break
  if all((p not in b[d]for d in b))and p==f(p)or p in(x,y):
   k+=[p]