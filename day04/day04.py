
data = [[[int(j) for j in i.split("-")] for i in l[:-1].split(",")] for l in open('day04/input.txt').readlines()]
print(len([x for x in data if (x[0][0] <= x[1][0] and x[0][1] >= x[1][1]) or (x[1][0] <= x[0][0] and x[1][1] >= x[0][1])]))
print(len([x for x in data if ((x[0][0] <= x[1][0] and x[0][1] >= x[1][0]) or (x[0][0] >= x[1][0] and x[0][1] <= x[1][0])
            or (x[1][0] <= x[0][0] and x[1][1] >= x[0][0]) or (x[1][0] >= x[0][0] and x[1][1] <= x[0][0]))]))