n,a = int(input()),int(input())
sum = 0
for i in range(1,n+1):
    sum+=( i * a )** (1/(i+1))
print(sum**0.5)
