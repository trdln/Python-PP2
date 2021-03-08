import io


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('test.txt','w') as txt:
    for i in color:
        txt.write("%s\n" % i)
    txt.write("End")
txt = open('test.txt')
print(txt.read())