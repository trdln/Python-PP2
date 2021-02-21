s = input()
print(s[2])
print(s[len(s)-2])
print(s[0:5])
print(s[0:-2])
i = 0
even = ''
odd = ''
while i < len(s):
    even+=s[i]
    i+=2
i = 1
while i < len(s):
    odd+=s[i]
    i+=2
print(even)
print(odd)
rev = lambda: s[::-1]
print(rev())
reveven = ''
i = 0
while i < len(rev()):
    reveven+=rev()[i]
    i+=2
print(reveven)
print(len(s))