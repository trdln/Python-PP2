from sys import setrecursionlimit
setrecursionlimit(2000)
n = int(input())
tree = {}
all = set()
childs = set()
for i in range(n-1):
    ch,par = input().split()
    all.add(ch)
    all.add(par)
    childs.add(ch)
    if tree.get(par,[]) != []:  tree[par].append(ch)
    else: tree[par] = [ch]
d = {}
def dfs(curr):
    cur = 1
    for ch in tree.get(curr,[]):
        cur += dfs(ch)
    d[curr]= cur -1
    return cur

main_par = all.difference(childs).pop()
dfs(main_par)
for i in sorted(d.items()):
    print(i[0],i[1])