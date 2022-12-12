for s in[['S'],['S', 'a']]:
 d=[l.strip()for l in open("day12/input.txt")]
 Q=[(i,j,0,'a')for i in range(len(d))for j in range(len(d[i]))if d[i][j]in s]
 v=set((i,j)for i,j,_,_ in Q)
 def p(i,j,k,a):
  if not 0<=i<len(d)or not 0<=j<len(d[i])or(i,j)in v:return
  b=d[i][j].replace('E','z')
  if ord(b)>ord(a)+1:return
  v.add((i,j))
  Q.append((i,j,k+1,b))
 while len(Q):
  i,j,k,a=Q.pop(0)
  if d[i][j]=='E':print(k)
  p(i+1,j,k,a)
  p(i-1,j,k,a)
  p(i,j+1,k,a)
  p(i,j-1,k,a)