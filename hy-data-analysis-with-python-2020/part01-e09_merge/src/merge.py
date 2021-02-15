#!/usr/bin/env python3

def merge(L1, L2):
    L3 = []
    x = 0
    y = 0
    while x < len(L1):
        if y == len(L2):
            L3.extend(L1[x:])
            break
        elif L1[x] <= L2[y]:
            L3.append(L1[x])
            x = x+1
        else:
            L3.append(L2[y])
            y = y+1
    L3.extend(L2[y:])
    return L3


def main():
    print(merge([3, 4, 5], [1, 2]))
    print(merge([1, 2], [3, 4, 5]))
    print(merge([1, 3, 5], [2, 4]))
    print(merge([1, 3, 5], [2, 4, 6]))


if __name__ == "__main__":
    main()
