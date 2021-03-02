l = [int(l) for l in input().split()]
mult = 1
for i in range(len(l)):
    mult*=l[i]
print(mult)