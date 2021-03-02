s = input()
s.replace(' ','')
uc,lc = 0,0
for i in s:
    if i.islower() == True:
        lc+=1
    elif i.isupper() == True: uc+=1
    else:pass
print(f'No. of Upper case characters : {uc}')
print(f'No. of Lower case Characters : {lc}')