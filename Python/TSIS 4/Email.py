import re
n = int(input())
for i in range(n):
    name, email = input().split(' ')
    if bool(re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>',email)):
        print(name,email)