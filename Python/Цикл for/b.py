a,b=int(input()),int(input())
arr = list()
if a < b:
    for i in range(a,b+1):
        print(i,end=" ")
else:
    a,b=b,a
    for i in range(a,b+1):
        arr.append(i)
    for i in reversed(arr):
        print(i,end=" ")