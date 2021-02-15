#!/usr/bin/env python3


def triple(x):
    return x*3


def square(x):
    return x**2


def main():
    for i in range(10):
        t = triple(i+1)
        s = square(i+1)
        if t < s:
            break
        print(f'triple({i+1})=={t} square({i+1})=={s}')


if __name__ == "__main__":
    main()
