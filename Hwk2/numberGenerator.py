import random
import sys

list1 = []
for i in range(10):
    file_name = 'set' + str(i) + '.txt'
    file = open(file_name, "w")
    for n in range(1):
        for i in range(10000):
            list1.append(random.randint(0,10000))
        for i in list1:
            file.write(str(i))
            file.write("\n")
        list1.clear()
    file.close
