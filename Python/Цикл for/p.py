a,b,c,d,e=int(input()),int(input()),int(input()),int(input()),int(input())
import math
sum = 0
for i in range(0,1001):
    if i == e: pass
    elif (a * math.pow(i,3) + b * math.pow(i,2) + c * i + d) / (i-e) == 0:
        sum+=1
print(sum) 