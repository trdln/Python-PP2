n,x = int(input()),float(input())
import math
sum = float(1)
for i in range(1,n+1):
    sum+=(((-1)**i) * (x ** (2 * i)))/(math.factorial(2*i))
print(sum)
