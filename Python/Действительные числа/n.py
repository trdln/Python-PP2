n = int(input())
sum = float(0)
for i in range(1,n+1):
    sum+=((-1)**(i+1)/(i))
print(sum)