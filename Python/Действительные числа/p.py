n = int(input())
sum = float(1)
for i in range(1,n+1):
    sum+=((-1)**i/(2*i+1))
print(4*sum)