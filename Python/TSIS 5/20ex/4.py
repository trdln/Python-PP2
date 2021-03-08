from os import read


def read_last(f,n):
    with open('test.txt','r') as txt:
        lines = txt.readlines()
        last_lines = lines[-n:]
        print(last_lines)

n=int(input())
read_last('test.txt',n)