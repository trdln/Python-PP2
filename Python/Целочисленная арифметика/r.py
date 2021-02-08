def rec(n,a,m):
    a=a+1
    if a == n: 
        return m
    if a % 2 != 0:
        return rec(n,a,m+5)
    else: 
        return rec(n,a,m+15)
n = int(input())
h,m =9,0
h +=(n * 45) // 60 
m +=(n* 45) % 60+rec(n,0,0)
if m >= 60:
    h += m // 60
    m %= 60
print(str(h)+" "+str(m))