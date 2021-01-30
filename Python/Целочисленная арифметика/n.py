n=int(input())
if n > 1440:
    while n > 1440:
        n -=1440
if n >= 60 and n<1440:
    m = n % 60
    h = int((n-m)/60)
    print(h,m)
elif n < 60:
    print(0,n)
else:
    print(0,0)

