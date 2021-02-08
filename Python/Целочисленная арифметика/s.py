a,b,n= int(input()),int(input()),int(input())
a*=n
b*=n
if b>=100:
    a+=b//100
    b%=100
print(str(a)+" "+str(b))