from colorama import Fore,Back,init,Style
init()
print(Back.CYAN)
print(Fore.BLACK)
print(Style.DIM)
fir = int(input("Введите число "))
one = 1
while(one>0):
    sec = int(input("Введите число "))
    sign = input("Что вы хотите сделать? ")
    if(sign == "+"):
        print(str(fir)+"+"+str(sec)+"=" + str(fir + sec))
        fir=fir+sec
    elif(sign == "-"):
        print(str(fir)+"-"+str(sec)+"=" + str(fir - sec))
        fir-=sec
    elif(sign == "*"):
        print(str(fir)+"*"+str(sec)+"=" + str(fir * sec))
        fir*=sec
    elif(sign == "/" ):
        if(sec != 0):
            print(str(fir)+"/"+str(sec)+"=" + str(int(fir / sec)))
            fir/=sec
        else:
            print("Недопустимо!")
    else:
        print("WRONG")
        one = -5
