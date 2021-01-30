a,b,c = int(input()),int(input()),int(input())
i = 0
if a==b:
    i+=1
    if a==c:
        i+=1
    if b == c:
        i+=1
else:
    if b==c:
        i+=1
    if a==c:
        i+=1
if i == 1:
    print(2)
else: print(i)