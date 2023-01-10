l=[x.split()for x in open('day15/input.txt').read().splitlines()]
d=[(x, y, abs(x-a) + abs(y-b)) for x,y,a,b in [(int(x[2][2:-1]), int(x[3][2:-1]), int(x[8][2:-1]), int(x[9][2:])) for x in l]]
A,B=2e6,4e6
print(max(x-abs(A-y)+i for x,y,i in d)-min(x+abs(A-y)-i for x,y,i in d))
f,t=lambda x,y,d,p,q,r:((p+q+r+x-y-d)//2,(p+q+r-x+y+d)//2+1),lambda x,y,p,q:abs(x-p)+abs(y-q)
print([B*X+Y for X,Y in[f(*a,*b)for a in d for b in d] if 0<X<B>Y>0 and all(t(X,Y,x,y)>i for x,y,i in d)])

    
