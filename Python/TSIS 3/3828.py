x = [int(x) for x in input().split()]
for i in range(len(x)):
    if i % 2==0:
        print(x[i],end=" ")