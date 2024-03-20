import numpy as np


def trace(matrix):
    return np.trace(matrix)

def main():
    A = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(trace(A))

if __name__ == '__main__':
    main()