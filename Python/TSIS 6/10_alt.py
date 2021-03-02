l = [int(l) for l in input().split()]
for i in range(len(l)):
    if l[i] & 1 == 0:
        print(l[i],end=" ")
    else:pass


l = list(format(lambda x: x & 1 == 0,l))
print(l)