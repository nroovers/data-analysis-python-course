#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    result = []
    with open(filename, "r") as f:
        for line in f:
            if len(line) > 0:
                print(line)
                match = re.search(r"(\d+)\s([A-Z][a-z][a-z])\s+(\d+)\s(\d\d):(\d\d)\s(\S*)\s\Z", line)
                result.append((
                    int(match.group(1)),
                    match.group(2),
                    int(match.group(3)),
                    int(match.group(4)),
                    int(match.group(5)),
                    match.group(6)))
    return result


def main():
    print(file_listing("src/listing.txt"))


if __name__ == "__main__":
    main()
