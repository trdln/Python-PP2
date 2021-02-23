import re
s = input()
rep = re.compile(r'(\d)\1*')
subs = r'\1'
print(rep.sub(subs,s))