x = [int(x) for x in input().split()]
mn = 1001
for i in range(len(x)):
    if x[i] > 0:
        if mn > x[i]:
            mn = x[i]
print(mn)