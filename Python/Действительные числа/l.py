a,b,c = int(input()),int(input()),int(input())
k = 0
if a == 0:
    SystemExit()
discr = b ** 2 - 4 * a * c
import math
l = []
if discr > 0:
    k = 2
    l.append(int((-b + math.sqrt(discr))/(2 * a)))
    l.append(int((-b - math.sqrt(discr))/(2 * a))) 
    print(k,*(sorted(l)))
elif discr == 0:
    k = 1
    l.append(int(-b / (2 * a)))
    print(k,*(sorted(l)))
elif c == 0:
    l.append(-b // a)
else: print(0)