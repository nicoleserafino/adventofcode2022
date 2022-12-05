data = open('day03/input.txt').read().strip().split('\n')
ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(sum([ascii_letters.index((set(i) & set(j)).pop()) + 1 for i, j in [(l[:len(l)//2], l[len(l)//2:]) for l in data]]))
print(sum([ascii_letters.index((set(i) & set(j) & set(k)).pop()) + 1 for i, j, k in [(data[x:x+3]) for x in range(0, len(data), 3)]]))