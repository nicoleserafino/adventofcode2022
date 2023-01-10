def s(e):
 a=m[e]
 return a[0] if len(a)==1 else"("+s(a[0])+a[1]+s(a[2])+")"
m={m:a.split(" ")for l in open("day21/input.txt").read().splitlines()for m,a in[l.split(": ")]}
print(int(eval(s("root"))))
m["humn"],m["root"][1]=["-1j"],"-("
c=eval(s("root")+")")
print(int(c.real / c.imag))