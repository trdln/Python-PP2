a,b = int(input()),int(input())
for i in range(a,b):
    if i//1000 == i%1000//100 == i%100//10 or i%1000//100 == i%100//10 == i %10 or i//1000 == i%100//10 == i %10 or i//1000 == i%1000//100 == i % 10:
        print(i)