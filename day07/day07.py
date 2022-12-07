for i in [x.split()for x in open("day07/input.txt")]:
    if i[0]=="dir"or i[1]=="ls":pass
    elif i[0]!='$':d[-1]+=int(i[0])
    elif i[2]=='..':
        s+=[d.pop()]
        d[-1]+=s[-1]
    elif i[2]=='/':s,d=[],[0]
    elif i[0]=="$"and i[1]=="cd":d.append(0)
print(sum(i for i in s+d[-1:]if i<=100000))
print(min(i for i in s+d[-1:]if i>(sum(d)-40000000)))