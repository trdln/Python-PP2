l = input().split()
n = l.count("0")
for i in filter(lambda x: x!="0",l):
    print(i,end=" ")
for i in range(n):
    print('0',end=" ")