s = input()
id = 0
l = []
for i in range(len(s)):
    if s[i] == 'f':
        id+=1
        l.append(i)
if id ==1:
    print(-1)
elif id>1:
    print(l[1])
else:
    print(-2)