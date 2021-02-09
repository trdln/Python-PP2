arr1 = [int(arr1) for arr1 in input().split()]
arr2 = [int(arr2) for arr2 in input().split()]
print(len(set(arr1)&set(arr2)))
