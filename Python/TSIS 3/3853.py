from collections import deque
def shift(key, array):
    a = deque(array) # turn list into deque
    a.rotate(key)    # rotate deque by key
    return list(a)   # turn deque back into a list
arr = [int(arr) for arr in input().split()]
steps = int(input())
arr = shift(steps, arr)
for i in arr:
    print(i,end=" ")