s = input()
l = []
for i in range(len(s)):
    if s[i]=='h':
        l.append(i)
print(s[0:l[0]]+s[l[len(l)-1]+1:])