from os import linesep, supports_effective_ids


def read_by(f):
    line = []
    with open('test.txt','r') as txt:
        for i in txt:
            line.append(i)
    print(line)
read_by('test.txt')