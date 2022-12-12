d=[x for x in open("day11/input.txt").read().splitlines()]
op=[(d[x][23:])for x in range(2,len(d),7)]
tst=[int(d[x][21:])for x in range(3,len(d),7)]
cn=[[int(d[x][29:]),int(d[x+1][30:])]for x in range(4,len(d),7)]
modulo=eval('*'.join(str(x)for x in tst))
for p in [20, 10000]:
 itm=[[[int(x)for x in(d[y][18:]).split(", ")]for y in range(1,len(d),7)]][0]
 ins=[0]*len(tst)
 for _ in range(p):
  for i in range(len(ins)):
   for j in range(0,len(itm[i])):
    c=itm[i][j]
    if op[i]=="* old":c*=c
    elif op[i][:2]in["* ","+ "]:c=eval(str(c)+op[i])
    c=c//3 if p==20 else c%modulo
    if c%tst[i]==0:itm[cn[i][0]].append(c)
    else:itm[cn[i][1]].append(c)  
    ins[i]+=1
   itm[i]=[]
 print(max(ins)*sorted(ins)[-2])