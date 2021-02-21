n = int(input())
l = []
l1 = []
for i in range(n-1):
    a = int(input())
    l.append(a)
for i in range(1,n+1):
    l1.append(i)
for i in l1:
    if i not in l:
        print(i,end=" ")
#set_dif = set(l1)-set(l)
#print(list(set_dif))
