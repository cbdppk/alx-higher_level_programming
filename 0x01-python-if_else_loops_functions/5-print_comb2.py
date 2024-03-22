#!/usr/bin/python3

for i in range(0, 100):
    if (i < 10):
        print("{}{}, ".format("0", i), end="")
    elif (i > 9 and i < 99):
        print("{}, ".format(i), end="")
    elif (i > 98):
        print("{}".format(i))
