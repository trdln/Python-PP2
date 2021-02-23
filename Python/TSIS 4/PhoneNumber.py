n = int(input())
import re
for i in range(n):
    if bool(re.match(r'[789]\d{9}$',input())):
        print("YES")
    else:print("NO")