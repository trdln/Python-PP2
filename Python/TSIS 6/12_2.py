s = input()
half = int(len(s)/2)
ok = False
for i in range(half-1):
    if s[i] == s[len(s)-1-i]:ok=True
    else:ok=False
print(ok)