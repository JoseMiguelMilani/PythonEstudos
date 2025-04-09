x = []
import random

for i in range (0,1000):
    num = random.randint(0,9)
    x.append(num)

    if num == 8:
        print(i)