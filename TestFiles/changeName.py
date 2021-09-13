import os
NUMBER = 2
print(NUMBER)
os.rename('local.txt', str(NUMBER))
NUMBER += 1
print(NUMBER)