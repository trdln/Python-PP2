#Main data types
nmbr = int(input())
fnmbr = float(nmbr)
arr = []
for i in range(0,nmbr):
    x = int(input())
    arr.append(x)
if type(nmbr)==int:
    print("True")
else: print("False")

