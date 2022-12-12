a=b=0;c=1;d=['\n']*6  
for e in sum(map(str.split,open('day10/input.txt')),[]):
 b+=c*-~a*(a%40==19)
 d[a//40]+=' #'[-2<c-a%40<2]
 a+=1
 c+=(e>'_'or int(e)+1)-1  
print(b,*d)