n,m = map(int,input().split())
a = [['.'] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if i & 1==0 and j & 1 != 0:
            a[i][j] = '*'
        elif i & 1 != 0 and j & 1 == 0:
            a[i][j] = '*'
for row in a:
    print(' '.join(row))