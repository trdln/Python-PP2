from shutil import copyfile
copyfile('test.txt','new.txt')
# if txt
txt = open('test.txt')
with open('new2.txt','a') as ntxt:
    ntxt.writelines(txt)
ntxt = open('new2.txt')
print(ntxt.readlines())