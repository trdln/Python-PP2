n = float(input())
import math
if n % 1 < 0.5:
    n = math.floor(n)
else: n = math.ceil(n)
print(n)