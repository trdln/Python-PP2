def rec(h,a,b,n,day):
    n+=a
    if n == h:
        return day
    else:
        return rec(h,a,b,n-b,day+1)
h,a,b=int(input()),int(input()),int(input())
print(rec(h,a,b,0,1))