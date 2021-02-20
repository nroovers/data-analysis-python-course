"""
A module for triangle calculations
"""

from math import sqrt

__version__ = '0.1'
__author__ = 'Nicolai Roovers'

def hypothenuse(a, b):
    """
    Returns the length of the hypothenuse when given the lengths of two other sides of a right-angled triangle.
    a: length of a side
    b: length of b side
    """
    return sqrt(a**2 + b**2)


def area(a, b):
    """
    Returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters.
    a: length of a side
    b: length of b side
    """
    c = hypothenuse(a, b)
    s = (a+b+c)/2
    return sqrt(s*(s-a)*(s-b)*(s-c))
