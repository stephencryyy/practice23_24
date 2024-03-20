import numpy as np


def circle_square(radius):
    return radius ** 2 * np.pi


def main():
    radius = float(input("Enter radius of circle: "))
    print(circle_square(radius))


if __name__ == '__main__':
    main()