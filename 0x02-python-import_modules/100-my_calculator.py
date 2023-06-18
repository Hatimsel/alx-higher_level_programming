#!/usr/bin/python3
import calculator_1 as compute
import sys
length = len(sys.argv)
result = 0
if __name__ == "__main__":
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = sys.argv[2]
        arg1 = int(sys.argv[1])
        arg2 = int(sys.argv[3])
        if operator == '+':
            result = int(compute.add(arg1, arg2))
            print("{:d} + {:d} = {:d}".format(arg1, arg2, result))
        elif operator == '-':
            result = int(compute.sub(arg1, arg2))
            print("{:d} - {:d} = {:d}".format(arg1, arg2, result))
        elif operator == '*':
            result = int(compute.mul(arg1, arg2))
            print("{:d} * {:d} = {:d}".format(arg1, arg2, result))
        elif operator == '/':
            result = int(compute.div(arg1, arg2))
            print("{:d} / {:d} = {:d}".format(arg1, arg2, result))
        else:
             print("Unknown operator. Available operators: +, -, * and /")
             exit(1)
