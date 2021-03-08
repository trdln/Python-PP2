import random
l = open('test.txt').readlines()
print(l[random.randint(0,len(l)-1)])


print(random.choice(open('test.txt').read().splitlines()))