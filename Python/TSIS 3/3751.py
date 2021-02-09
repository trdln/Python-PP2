s = set(input().split()) & set(input().split())
print(*sorted(s,key=int))