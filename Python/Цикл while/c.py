import math
n = int(input())
for i in range(n+1):
    for j in range(int(math.sqrt(n))):
        if 2 ** j == i:
            print(i,end=" ")