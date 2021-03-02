n = int(input())
a = [[0]*n for i in range(n)]
k = 1
while k < n + 1:
    for i in range(n):
        for j in range(n):
            if i == n - j - 1:
                a[i][j] = 1
            elif i - k + 1 == n - j - 1:
                a[i][j] = 2
    k+=1
for i in range(n):
    for j in range(n):
        print(a[i][j],end=" ")
    print()