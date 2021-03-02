n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
b = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        b[i][j] = a[j][i]
for i in range(n):
    for j in range(n):
        print(b[i][j],end= " ")
    print()