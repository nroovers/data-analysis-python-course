#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    print(triangle.__version__)
    print(triangle.__author__)
    print(triangle.hypothenuse(5,4))
    print(triangle.area(5,4))

if __name__ == "__main__":
    main()
