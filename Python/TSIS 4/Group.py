import re
m = re.findall(r"([A-Za-z0-9])\1+",input()) #\1 чтоб найти одиноковые элементы
if m:
    print(m[0])
else:
    print(-1)