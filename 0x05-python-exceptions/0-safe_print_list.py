#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = b = 0
    for i in my_list:
        a += 1
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            b += 1
        except IndexError:
            break
    print("")
    return b
