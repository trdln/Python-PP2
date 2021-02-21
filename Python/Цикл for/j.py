n = int(input())
sum = 0
l = []
for i in range(1,n+1):
    l.append(i)   
k = ""
for i in range(1,len(l)):
    sum+=l[i]*l[i-1]
    k+=(str(l[i-1]) + "*" + str(l[i])+'+')
print(k[0:len(k)-1],'=',sum,sep='')