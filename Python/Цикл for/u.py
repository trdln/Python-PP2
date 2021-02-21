a,b = int(input()),int(input())
for i in range(a,b+1):
    if i//1000 == i % 10 and i%1000//100 == i%100//10:
        print(i)