c={tuple(map(int,l.split(',')))for l in open('day18/input.txt')}
s=lambda x,y,z:{(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)}
print(sum((i not in c)for j in c for i in s(*j)))
v=set()
t=[(-1,-1,-1)]
while t:
 h=t.pop()
 t+=[i for i in(s(*h)-c-v)if all(-1<=j<=25 for j in i)]
 v|={h}
print(sum((i in v)for j in c for i in s(*j)))