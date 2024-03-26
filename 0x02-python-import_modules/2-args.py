#!/usr/bin/python3
import sys


def main():
    args = sys.argv
    num_args = len(args)
    if (num_args < 2):
        print("{} arguments.".format(0))
    elif (num_args == 2):
        print("{} argument:".format(num_args-1))
        print("{}: {}".format(num_args-1, args[1]))
    elif (num_args > 2):
        print("{} arguments:".format(num_args-1))
        for i in range(1, num_args):
            print("{}: {}".format(i, args[i]))


if __name__ == "__main__":
    main()
