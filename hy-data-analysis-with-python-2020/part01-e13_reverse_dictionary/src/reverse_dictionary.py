#!/usr/bin/env python3

def reverse_dictionary(d):
    rev={}
    for eng, finL in d.items():
        for fin in finL:
            if fin in rev:
                rev[fin].append(eng)
            else:
                rev[fin]=[eng]
    return rev


def main():
    d = {'move': ['liikuttaa'], 'hide': ['piilottaa',
                                         'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()
