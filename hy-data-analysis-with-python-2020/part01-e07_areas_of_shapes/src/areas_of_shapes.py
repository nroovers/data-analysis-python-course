#!/usr/bin/env python3

import math


def triangle():
    base = input('Give base of the triangle: ')
    height = input('Give height of the triangle: ')
    return (float(base)*float(height))/2


def rectangle():
    width = input('Give base of the rectangle: ')
    height = input('Give height of the rectangle: ')
    return float(width)*float(height)


def circle():
    radius = input('Give radiua of the circle: ')
    return math.pi*float(radius)**2


def main():
    while True:
        option = input('Choose a shape (triangle, rectangle, circle): ')
        area = 0
        if option == 'triangle':
            area = triangle()
        elif option == 'rectangle':
            area = rectangle()
        elif option == 'circle':
            area = circle()
        elif option == '':
            break
        else:
            print('Unknown shape!')
            continue
        print(f'The area is {area:.6f}')


if __name__ == "__main__":
    main()
