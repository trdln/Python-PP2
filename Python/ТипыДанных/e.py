import math
n = 10
pi,ad = 0,0
for i in range(1,n+1):
    ad += 1 / i**2
pi = math.sqrt(ad*6)
print(pi)