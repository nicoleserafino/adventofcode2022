directions = [[int(x) for x in line.split() if x.isdigit()] for line in open("day05/input.txt").read().split("\n") if line.startswith("move")]
stacks = [[row[k] for row in [line[1:][::4] for line in open("day05/input.txt").read().split("\n") if "[" in line] if row[k] != " "] for k in range(9)]
stacks2 = stacks[:]
for i in directions:
    amt, src, dest = i[0], i[1] - 1, i[2] - 1
    stacks[dest] = stacks[src][:amt][::-1] + stacks[dest]
    stacks[src] = stacks[src][amt:]
    stacks2[dest] =  stacks2[src][:amt] + stacks2[dest]
    stacks2[src] = stacks2[src][amt:]
print("".join(stack[0] for stack in stacks))
print("".join(stack[0] for stack in stacks2))