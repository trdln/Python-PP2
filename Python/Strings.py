nameandsurname = [input(),input()]
if nameandsurname[0][0].isupper == True:
    print("Correct")
else:
    print("Not correct")
if nameandsurname[1][0].isupper == True:
    print("Correct")
else:
    print("Not correct")
for char in nameandsurname[0]:
    print(char)
print(len(nameandsurname[0]),len(nameandsurname[1]))
if "Nurassyl" in nameandsurname[0]:
    print("All for eyes")
else: 
    print("Just for fun")


