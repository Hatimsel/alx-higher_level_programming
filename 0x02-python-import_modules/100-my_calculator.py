#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

argv = sys.argv
args_num = len(argv)
if __name__ == "__main__":
    if args_num != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] == "+":
        #result = int(add(argv[1], argv[3]))
        result = int(add(int(argv[1]), int(argv[3])))
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
    elif argv[2] == "-":
        #result = int(sub(argv[1], argv[3]))
        result = int(sub(int(argv[1]), int(argv[3])))
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
    elif argv[2] == "*":
        #result = int(mul(argv[1], argv[3]))
        result = int(mul(int(argv[1]), int(argv[3])))
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
    elif argv[2] == "/":
        #result = int(div(argv[1], argv[3]))
        result = int(div(int(argv[1]), int(argv[3])))
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
    else:
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit(1)
