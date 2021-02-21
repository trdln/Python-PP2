st = input()
f,s='',''
siz = int(len(st))
div = int((siz-1)//2+1)
f = st[0:div]
s = st[div:siz]
print(s,f,sep="")