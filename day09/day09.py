x=[(A,int(B))for A,B in[l.strip().split()for l in open("day09/input.txt")]]
ds={"U":(0,1),"D":(0,-1),"L":(-1,0),"R":(1,0)}
hl=tl=(0,0)
ks=[hl]*10
for p in [0,1]:
 ts={(0,0)}
 for d,n in x:
  dx,dy=ds[d]
  for i in range(n):
   hx,hy=hl if p==0 else ks[0]
   tx,ty=tl
   hx,hy=hx+dx,hy+dy
   if p==1:ks[0]=(hx,hy)
   for k in range(9) if p==1 else []:
    hx,hy=ks[k]
    tx,ty=ks[k+1]
    if abs(hx-tx)>=2 or abs(hy-ty)>=2:
     tdx,tdy=1,1
     tdx=0 if hx-tx==0 else -1 if hx-tx<0 else 1
     tdy=0 if hy-ty==0 else -1 if hy-ty<0 else 1
     tx,ty=tx+tdx,ty+tdy
     ks[k+1]=(tx,ty)
     if k==8:ts|={(tx,ty)}
   if(abs(hx-tx)>=2 or abs(hy-ty)>=2)and p==0:tl=hl;ts|={(tl)}
   hl=(hx, hy)
 print(len(ts))