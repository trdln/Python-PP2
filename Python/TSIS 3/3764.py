print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except:
        break
    contents.append(line)
d = {}
words=[]
for i in range(len(contents)):