l = input().split()
k = int(input())
k %= len(l)
# print(l[-k:],l[:-k])
for i in l[-k:]+l[:-k]:
    print(i,end=" ")
