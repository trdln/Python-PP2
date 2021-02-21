s = input()
nw = ""
for i in range(len(s)):
    if i % 3!=0:
        nw += s[i]
print(nw)