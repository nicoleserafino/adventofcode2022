d=open("day06/input.txt").read()
print([[i for i in range(j,len(d))if len(set(d[i-j:i]))==j][0]for j in[4,14]])