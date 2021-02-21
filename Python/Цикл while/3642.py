import math
n = int(input())
l = []
for i in range(n+1):
    for j in range(1,int(math.sqrt(n))+1):
        if j*j==i:
            l.append(i)
print(*(l))