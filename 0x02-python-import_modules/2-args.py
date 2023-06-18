#!/usr/bin/python3
import sys
argv = sys.argv
length = len(argv)
n = 1
if __name__ == "__main__":
    if length == 1:
        print("0 arguments")
    elif length == 2:
        print("1 argument:")
        print("1: {:s}".format(argv[1]))
    else:
        print("{:d} arguments:".format(length - 1))
        for i in range(1, length):
            print("{:d}: {:s}".format(n, argv[i]))
            n += 1
