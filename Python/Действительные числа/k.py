a,b,c = int(input()),int(input()),int(input())
if a == 0:
    SystemExit()
discr = b ** 2 - 4 * a * c
import math
l = []
if discr > 0:
    l.append(int((-b + math.sqrt(discr))/(2 * a)))
    l.append(int((-b - math.sqrt(discr))/(2 * a))) 
elif discr == 0:
    l.append(int(-b / (2 * a)))
elif c == 0:
    l.append(-b // a)
else: pass
print(*(sorted(l)))