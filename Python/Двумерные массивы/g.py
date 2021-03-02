def is_symmetric(a):
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                return False
    return True
 
n = int(input())
A =[[int(j) for j in input().split()] for i in range(n)]
if is_symmetric(A):
    print('YES')
else:
    print('NO')