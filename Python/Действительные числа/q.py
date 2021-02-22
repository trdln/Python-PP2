n,x = int(input()),float(input())
import math
sum = float(1)
for i in range(1,n+1):
    sum+=(x**i)/(math.factorial(i))
print(sum)
