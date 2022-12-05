d=[[int(x)for x in line.split()if x.isdigit()]for line in open("day05/input.txt").read().split("\n")if line.startswith("move")]
s=[[row[k]for row in [line[1:][::4]for line in open("day05/input.txt").read().split("\n")if"["in line]if row[k]!=" "]for k in range(9)]
s2=s[:]
for i in d:
    a,f,t=i[0],i[1]-1,i[2]-1
    s[t]=s[f][:a][::-1]+s[t]
    s[f]=s[f][a:]
    s2[t]=s2[f][:a]+s2[t]
    s2[f]=s2[f][a:]
print("".join(x[0]for x in s))
print("".join(x[0]for x in s2))