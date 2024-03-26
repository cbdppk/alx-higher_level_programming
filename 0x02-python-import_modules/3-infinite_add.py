#!/usr/bin/python3
import sys


def main():
    args = sys.argv
    num_args = len(args)
    if (num_args == 1):
        print("{}".format(0))
    elif (num_args > 1):
        for i in range(1, num_args):
            added = 0
            added += int(args[i])
        print("{}".format(added))


if __name__ == "__main__":
    main()
