def file_read(fname,n):
    from itertools import islice
    with open (fname) as txt:
        for i in islice(txt,n):
            print(i)
n = int(input())
file_read('test.txt',n)