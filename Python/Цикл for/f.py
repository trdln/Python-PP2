n,k = int(input()),int(input())
a,b,c = 1,1,1
d = n - k
while n > 1:
    a *= n
    n-=1
while k > 1:
    b *= k
    k-=1
while d>1:
    c*=d
    d-=1
print(int(a/(b*c)))