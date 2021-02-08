h1,m1,s1,h2,m2,s2=int(input()),int(input()),int(input()),int(input()),int(input()),int(input())
f,s=0,0
f+=h1*3600+m1*60+s1
s+=h2*3600+m2*60+s2
print(s-f)