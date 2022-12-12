for i,j,*k in map(str.split,open("day07/input.txt")):
 if i=="dir"or j=="ls":0
 elif i!='$':d[-1]+=int(i)
 elif '..'in k:
  s+=[d.pop()]
  d[-1]+=s[-1]
 elif '/'in k:s,d=[],[0]
 elif j=="cd":d+=[0]
print(sum(i for i in s+d[-1:]if i<=100000))
print(min(i for i in s+d[-1:]if i>(sum(d)-40000000)))