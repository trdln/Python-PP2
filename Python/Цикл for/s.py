n = int(input())
for i in range(99,1000):
    if i//100 + i % 100 //10 + i % 10 == n:
        print(i)