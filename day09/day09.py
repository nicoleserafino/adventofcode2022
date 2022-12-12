d_list=[(A,int(B))for A,B in[l.strip().split()for l in open("day09/input.txt")]]
dirs={"U":(0,1),"D":(0,-1),"L":(-1,0),"R":(1,0)}
headloc,tailloc=(0,0),(0,0)
knots=[(0,0)]*10
for p in range(2):
 tailset=set((0,0))
 for d,n in d_list:
  dx,dy=dirs[d]
  for i in range(n):
   hx,hy=headloc if p==0 else knots[0]
   tx,ty=tailloc
   hx,hy=hx+dx,hy+dy
   if p==1:knots[0]=(hx,hy)
   for k in range(9) if p==1 else range(0):
    hx,hy=knots[k]
    tx,ty=knots[k+1]
    if abs(hx-tx)>=2 or abs(hy-ty)>=2:
     tdx,tdy=1,1
     if hx-tx==0:tdx=0
     elif hx-tx<0:tdx=-1
     if hy-ty==0:tdy=0
     elif hy-ty<0:tdy=-1
     tx,ty=tx+tdx,ty+tdy
     knots[k+1]=(tx,ty)
     if k==8:tailset.add((tx,ty))
   if(abs(hx-tx)>=2 or abs(hy-ty)>=2)and p==0:
    tailloc=headloc
    tailset.add(tailloc)
   headloc=(hx, hy)
 print(len(tailset))