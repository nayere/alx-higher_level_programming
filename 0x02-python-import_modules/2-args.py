#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argLen = len(sys.argv)
    if argLen == 1:
        print("No arguments provided.")
    elif argLen == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(argLen - 1))

    for i, arg in enumerate(sys.argv[1:], 1):
        print("{}: {}".format(i, arg))


