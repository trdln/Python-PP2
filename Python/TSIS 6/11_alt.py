n = int(input())
l = []
for i in range(1,n):
    if n % i == 0:
        l.append(i)
if n == sum(l):
    print(f'{n} is perfect number')
else:print(f'{n} is not perfect number')