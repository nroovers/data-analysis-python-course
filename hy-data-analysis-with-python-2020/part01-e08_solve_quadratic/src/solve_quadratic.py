#!/usr/bin/env python3

import math


def solve_quadratic(a, b, c):
    sqrt = math.sqrt((b**2)-(4*a*c))
    return ((-b+sqrt)/(2*a), (-b-sqrt)/(2*a))


def main():
    print(solve_quadratic(1, -3, 2))
    print(solve_quadratic(1, 2, 1))


if __name__ == "__main__":
    main()
