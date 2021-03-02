n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
k = int(input())
l = []
for i in range(n):
    for j in range(n):
        if i == j+k:
            l.append(a[i][j])
print(*l)