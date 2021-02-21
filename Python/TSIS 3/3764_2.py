d = {}
def cmp(item):
    return (-item[1],item[0])
try:
    while True:
        line=input().split()
        for word in line:
            if d.get(word,0) != 0: d[word] += 1
            else: d[word]=1
except:
    for i in sorted(d.items(),key = cmp):
        print(i[0])
