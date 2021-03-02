n, m = (int(_) for _ in input().split())
A = [[int(elem) for elem in input().split()] for r in range(n)]
idxi, idxj = 0, 0
maxelem = A[0][0]
for i in range(n):
  for j in range(m):
    if A[i][j] > maxelem:
      maxelem = A[i][j]
      idxi = i
      idxj = j
print (idxi, idxj)