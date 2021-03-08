with open('test.txt','w') as txt:
    append_txt = input()
    txt.write(append_txt)
output = open('test.txt')
print(output.read())