#!/usr/bin/env python3
import re


def file_extensions(filename):
    noext = []
    exts = {}
    with open(filename, "r") as f:
        for line in f:
            match = re.search(r"\S+\.(\w+)", line)
            if match != None:
                ext = match.group(1)
                if ext in exts:
                    exts[ext].append(line.strip())
                else:
                    exts[ext] = [line.strip()]
            else:
                noext.append(line.strip())
    return (noext, exts)


def main():
    result = file_extensions("src/filenames.txt")
    print(f'{len(result[0])} files with no extension')
    for ext in sorted(result[1].keys()):
        print(f'{ext} {len(result[1][ext])}')


if __name__ == "__main__":
    main()
