def isjai(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
n = int(input())
for i in range(2,n+1):
    if n % i == 0 and isjai(i):
        print(i)
        quit()
