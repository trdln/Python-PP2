import os
print(os.stat('test.txt'))
print(os.stat('test.txt').st_size)