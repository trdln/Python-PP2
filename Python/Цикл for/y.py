n = int(input())
cur = 1
k = 0
for i in range(n):
   print(cur, end=' ', flush=True)
   k = k + 1
   if k == cur:
       k = 0
       cur = cur + 1
print()