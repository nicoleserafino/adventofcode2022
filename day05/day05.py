d=[[int(x)for x in l.split()if x.isdigit()]for l in open("day05/input.txt").read().split("\n")if l.startswith("move")]
s=[[r[k]for r in [l[1::4]for l in open("day05/input.txt").read().split("\n")if"["in l]if r[k]!=" "]for k in range(9)]
z=s[:]
for i in d:
    a,f,t=i[0],i[1]-1,i[2]-1
    s[t]=s[f][:a][::-1]+s[t]
    s[f]=s[f][a:]
    z[t]=z[f][:a]+z[t]
    z[f]=z[f][a:]
print("".join(x[0]for x in s))
print("".join(x[0]for x in z))