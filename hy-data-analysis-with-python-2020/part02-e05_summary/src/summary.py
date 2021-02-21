#!/usr/bin/env python3

import sys
import math


def summary(filename):
    floats = []
    with open(filename, "r") as f:
        for s in f:
            try:
                floats.append(float(s))
            except ValueError:
                continue

    sum = math.fsum(floats)
    avg = sum/len(floats)
    sd = math.sqrt(
        math.fsum([(x-avg)**2 for x in floats]) / (len(floats)-1))
    return (sum, avg, sd)


def main():
    for file in sys.argv[1:]:
        result = summary(file)
        print(f"File: {file} Sum: {result[0]:6f} Average: {result[1]:6f} Stddev: {result[2]:6f}")


if __name__ == "__main__":
    main()
