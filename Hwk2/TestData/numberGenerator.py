import random
import sys

list1 = []
file = open("set9.txt", "w")
for n in range(1):
    for i in range(1000000):
       list1.append(random.randint(0,10))
    for i in list1:
        file.write(str(i))
        file.write("\n")
    list1.clear()

file.close
