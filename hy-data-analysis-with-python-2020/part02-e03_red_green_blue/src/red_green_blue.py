#!/usr/bin/env python3

import re


def red_green_blue(filename="src/rgb.txt"):
    result = []
    with open(filename, "r") as f:
        f.readline()
        for line in f:
            match = re.search(
                r"\s*(\d+)\s+(\d+)\s+(\d+)\s[\t]+(.*)\s", line)
            s=f"{match.group(1)}\t{match.group(2)}\t{match.group(3)}\t{match.group(4)}"
            result.append(s)
    return result


def main():
    print(red_green_blue())


if __name__ == "__main__":
    main()
