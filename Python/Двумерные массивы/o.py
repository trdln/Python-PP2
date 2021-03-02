s = input()
a = [['.'] * 8 for i in range(8)]
fr , sc = s[0],int(s[1])
d = {"a" : 0,'b' : 1, 'c' : 2 , 'd' : 3, 'e' : 4, 'f' : 5, 'g':6,'h':7}
a[8 - sc][d[fr]] = 'K'
for i in range(8):
    for j in range(8):
        if   0<= 8 - sc + 1 <=7  and 0<=d[fr]+2<=7:
            a[8 - sc + 1][d[fr] + 2] = '*'

        if   0<= 8 - sc + 2 <= 7  and 0<=d[fr]+1<=7:
            a[8 - sc + 2][d[fr] + 1] = '*'

        if   0<= 8 - sc - 1 <= 7  and 0<=d[fr]+2 <=7:
            a[8 - sc - 1][d[fr] + 2] = '*'

        if   0<= 8 - sc - 2 <= 7  and 0<=  d[fr] + 1 <=7:
            a[8 - sc - 2][d[fr] + 1] = '*'

        if   0<= 8 - sc - 1 <= 7 and 0<=  d[fr] - 2 <=7:
            a[8 - sc - 1][d[fr] - 2] = '*'

        if   0<= 8 - sc - 2 <= 7  and 0<=  d[fr] - 1 <=7:
            a[8 - sc - 2][d[fr] - 1] = '*'

        if   0<= 8 - sc + 1 <= 7 and 0<=  d[fr] - 2 <=7:
            a[8 - sc + 1][d[fr] - 2] = '*'

        if 0<=8 - sc + 2  <= 7 and 0<=  d[fr] - 1  <=7:
            a[8 - sc + 2][d[fr] - 1] = '*'

for i in range(8):
    for j in range(8):
        print(a[i][j],end=' ')
    print()