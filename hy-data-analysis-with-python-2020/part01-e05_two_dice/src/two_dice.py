#!/usr/bin/env python3

def main():
    dice = [1, 2, 3, 4, 5, 6]
    for i in dice:
        for j in dice:
            if i+j == 5:
                print(f'({i}, {j})')


if __name__ == "__main__":
    main()
