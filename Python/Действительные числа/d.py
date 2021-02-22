a,b,c = int(input()),int(input()),int(input())
p = ((a+b+c)/2)
s = p*(p-a)*(p-b)*(p-c)
print(s**0.5)