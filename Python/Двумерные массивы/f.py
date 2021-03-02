n,m = map(int,input().split())
a = [[int(j) for j in input().split()] for i in range(n)]
ind,ji = map(int, input().split())
k = 0
while k < n:
    a[k][ind],a[k][ji] = a[k][ji],a[k][ind]
    k+=1
for i in range(n):
    for j in range(m):
        print(a[i][j],end=" ")
    print()

