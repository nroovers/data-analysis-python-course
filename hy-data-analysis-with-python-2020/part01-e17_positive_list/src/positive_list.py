#!/usr/bin/env python3

def positive_list(L):
    def isPos(x):
        return x > 0

    return list(filter(isPos, L))


def main():
    print(positive_list([2, -2, 0, 1, -7]))


if __name__ == "__main__":
    main()
