print(max(sum(map(int,x.split()))for x in open('day01/input.txt').read().split('\n\n')))
print(sum(sorted(sum(map(int,x.split()))for x in open('day01/input.txt').read().split('\n\n'))[-3:]))