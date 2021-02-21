s = input()
id = 0
l = []
for i in range(len(s)):
    if s[i] == 'f':
        id+=1
        l.append(i)
if id ==1:
    print(*(l))
elif id>1:
    print(l[0],l[len(l)-1])
else:
    pass