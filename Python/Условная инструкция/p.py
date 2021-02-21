a=int(input())
b=int(input())
a = float(a)
b = float(b)
if a==0 and b==0:
    print('INF')
elif a!=0 and (b==0 or abs(a)<=abs(b)) and (b % a) == 0:
    print(int(-b/a))
else:
    print('NO')