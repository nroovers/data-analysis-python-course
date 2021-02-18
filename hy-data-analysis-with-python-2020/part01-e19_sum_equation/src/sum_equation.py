#!/usr/bin/env python3
from functools import reduce


def sum_equation(L):
    s1='0'
    s2='0'
    if len(L)>0:
        s1 = ' + '.join(str(s) for s in L)
        s2 = str(reduce(lambda x, y: x+y, L, 0))
    return " = ".join([s1, s2])


def main():
    print(sum_equation([1, 5, 7]))
    print(sum_equation([]))


if __name__ == "__main__":
    main()
