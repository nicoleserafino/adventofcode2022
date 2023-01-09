x=lambda s:x(s[:-1])*5+'=-012'.find(s[-1])-2 if s else 0
y=lambda d:y((d+2)//5)+'=-012'[(d+2)%5]if d else''
print(y(sum(map(x,open('day25/input.txt').read().split()))))