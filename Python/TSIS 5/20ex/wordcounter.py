l = input().split()
st = list(set(l))
d = {}
for i in l:
    d[i] = l.count(i)
for k,v in d.items():
    print(f'The freq of "{k}" is !{v}! times')