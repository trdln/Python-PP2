s = input()
ok = False
if len(s)%2==0:
    f,sec = s[0:int((len(s))/2)],s[int((len(s))/2):]
    if f == sec:
        print(f'{s} is palindrome')
    else:
        print(f'{s} is not palindrome')
else:
    f,sec = s[0:int((len(s)-1)/2)],s[int((len(s)+1)/2):]
    if f == sec:
        print(f'{s} is palindrome')
    else:
        print(f'{s} is not palindrome')    