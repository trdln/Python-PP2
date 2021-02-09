x = [int(x) for x in input().split()]
arr = list()
for i in reversed(x):
    if i == 0:
        x.append(i)
        x.pop(i)
for i in x:
    print(i,end=" ")