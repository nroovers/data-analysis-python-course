#!/usr/bin/env python3

def detect_ranges(L):
    result=[]
    ranges = [[]]
    for i in sorted(L):
        # print('nr', i)
        if len(ranges[-1]) == 0 or ranges[-1][-1]+1 == i:
            ranges[-1].append(i)
            # print('appended to range', ranFge)
        else:
            ranges.append([i])
            # print('range appended to result', ranges)
    for r in ranges:
        if len(r)==1:
            result.append(r[0])
        else:
            result.append((r[0],r[-1]+1))
    return result


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
