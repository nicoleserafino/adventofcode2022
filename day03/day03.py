d=open('day03/input.txt').read().strip().split('\n')
x="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(sum([x.index(({*i}&{*j}).pop())+1 for i,j in[(l[:len(l)//2],l[len(l)//2:])for l in d]]))
print(sum([x.index(({*i}&{*j}&{*k}).pop())+1 for i,j,k in[(d[x:x+3])for x in range(0,len(d),3)]]))