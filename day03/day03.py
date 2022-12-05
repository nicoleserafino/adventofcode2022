data = open('day03/input.txt').read().strip().split('\n')
ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(sum([ascii_letters.index((set(a) & set(b)).pop()) + 1 for a, b in [(line[:len(line)//2], line[len(line)//2:]) for line in data]]))
print(sum([ascii_letters.index((set(a) & set(b) & set(c)).pop()) + 1 for a, b, c in [(data[i:i+3]) for i in range(0, len(data), 3)]]))