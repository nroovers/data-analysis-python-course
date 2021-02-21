#!/usr/bin/env python3

import sys


def file_count(filename):
    lines = 0  # number of lines, words, and characters
    words = 0
    chars = 0
    with open(filename, "r") as f:
        for line in f:
            lines += 1
            words += len(line.split())
            chars += (len(line))

    return (lines, words, chars)


def main():
    # print(file_count("src/test.txt"))
    for file in sys.argv[1:]:
        result = file_count(file)
        print(f"{result[0]}\t{result[1]}\t{result[2]}\t{file}")


if __name__ == "__main__":
    main()
