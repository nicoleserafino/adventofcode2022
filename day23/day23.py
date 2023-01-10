e={complex(x,y)for x,r in enumerate(open('day23/input.txt'))for y,c in enumerate(r)if c=='#'}
dirs=(-1,1,-1j,1j)
adjs=dirs+(-1-1j,1-1j,-1+1j,1+1j)
for r in range(1, 1e6):
 plan=lambda l:next((l+k for k in dirs if not any(l+k+k*x in e for x in (0,1j,-1j))and any(l+i in e for i in adjs)), None)
 my_list=list(map(plan, e))
 plans={item:my_list.count(item)for item in my_list}
 moves=[(l,plan(l))for l in e if plans[plan(l)]==1]
 if not moves:print(r);break 
 src,dst=map(set,zip(*moves))
 e=e-src|dst
 dirs=dirs[1:]+dirs[:1]
 if r==10:
  a,*_,b=sorted(l.real for l in e)
  c,*_,d=sorted(l.imag for l in e)
  print((b-a+1)*(d-c+1)-len(e))