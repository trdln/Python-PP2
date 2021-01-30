import math
n = 10
pi,ad,da = 0,0,0
for i in range(1,n+1):
    ad += 1 / pow(i,2)
da = 6 * ad
pi = math.sqrt(da)
print(pi)