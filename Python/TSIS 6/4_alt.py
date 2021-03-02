def rev(s):
    rs = ''
    i = 0
    while i < len(s):
        rs+=s[len(s)-i-1]
        i+=1
    return rs
print(rev(input()))