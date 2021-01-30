n = 10
pi = 0
lst1 = []
for i in range(0,n*2):
    if(i % 2 != 0):
        lst1.append(i)
for i in range(len(lst1)):
    if(i % 2 == 0):
        pi+= 4/lst1[i]
    else:
        pi-=4/lst1[i]
print(pi)