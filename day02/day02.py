d = {'A':0,'B':1,'C':2,'X':0,'Y':1,'Z':2}
turns = [[d[x] for x in l.split()] for l in open("day02/input.txt").read().split("\n")]
print(sum(b+1+(b-a+1)%3*3 for a, b in turns))
print(sum((b+a-1)%3+1+b*3 for a, b in turns))