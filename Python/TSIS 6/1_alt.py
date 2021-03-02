def findmax(a,b,c):
    if a > b: 
        if a > c:
            return a
        else: return c
    else:
        if b > c:
            return b
        else: return c
a,b,c = int(input()),int(input()),int(input())
print(findmax(a,b,c))
    