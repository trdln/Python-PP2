arr = [int(arr) for arr in input().split()]
steps = int(input())
if steps < 0:
    for i in range(abs(steps)):
        arr.append(arr.pop(0))
else:
    for i in range(steps):
        arr.insert(0,arr.pop())
for i in arr:
    print(i,end=" ")