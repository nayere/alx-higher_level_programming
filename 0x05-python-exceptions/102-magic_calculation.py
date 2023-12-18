#!/usr/bin/python3
def magic_calculation(x, y):
    from magic_calculation_102 import add, sub

    if (x < y):
        z = add(x, y)

        for w in (range(4, 6)):
            z = add(z, w)
        return (z)

    else:
        return (sub(x, y))
