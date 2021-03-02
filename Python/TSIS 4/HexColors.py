import re

n = int(input())
colors = []
for i in range(n):
    s = input()
    if len(s) > 7:
        colors.append(re.findall(r'(#[0-9a-fA-F]{3,6})',s))
for elem in colors:
    for el in elem:
        print(el)