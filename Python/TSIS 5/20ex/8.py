txt = open('test.txt')
words = txt.read().split()
mx = -1
lnw = ''
for i in range(len(words)):
    if len(words[i]) > mx:
        lnw = words[i]
        mx = len(words[i])
print(lnw)