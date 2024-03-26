#!/usr/bin/python3
import sys


def main():
    args = sys.argv
    num_args = len(args)
    if (num_args == 1):
        print("{}".format(0))
    elif (num_args > 1):
        added = 0
        for i in range(1, num_args):
            num = int(args[i])
            added += num
        print("{}".format(added))


if __name__ == "__main__":
    main()
