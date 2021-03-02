n = int(input())
a = [[0]*n for i in range(n)]
k = 1
while k < n+1:
    for i in range(n):
        for j in range(n):
            if i+k==j or i-k==j:
                a[i][j]=k
    k+=1
for i in range(n):
    for j in range(n):
        print(a[i][j],end=" ")
    print()