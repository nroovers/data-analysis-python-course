#!/usr/bin/env python3

def toInt(s):
    return int(s)


def transform(s1, s2):
    L1 = list(map(toInt, s1.split()))
    L2 = list(map(toInt, s2.split()))
    return [t[0]*t[1] for t in zip(L1, L2)]


def main():
    print(transform("1 5 3", "2 6 -1 3"))


if __name__ == "__main__":
    main()
