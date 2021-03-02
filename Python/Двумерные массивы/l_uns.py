n,m = map(int, input().split())
a = [[int(j) for j in input().split()] for i in range(n)]
ok = False
id = 0
k = 0
s = int(input())
while k < s:
    for i in range(n):
        for j in range(m-1):
            if a[i][j+k] == 0:
                ok = True
    if ok:
        id = i
    else: ok = False
    k+=1      
if ok == False:
    print(0)
else: print(id)