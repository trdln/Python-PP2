import re
v = "aeiouAEIOU"
c = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
print(*re.findall("(?=[%s]([%s]{2,})[%s])"%(c,v,c),input(), re.I) or [-1], sep="\n")