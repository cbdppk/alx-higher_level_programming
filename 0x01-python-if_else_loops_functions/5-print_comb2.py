#!/usr/bin/python3

for i in range(0, 100):
    if (i < 98):
        print("{0:02}, ".format(i), end="")
    elif (i > 98):
        print("{}".format(i))
