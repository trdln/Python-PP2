v = int(input())
t = int(input())
s = (abs(109 - abs(v * t)))
while s >= 109:
    s -= 109
print(s)