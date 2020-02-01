import numpy as np

from matrix import Matrix


def main():
    a = Matrix([[1, 2, 3], [4, 5, 6]])
    b = Matrix([[1, 0, 0], [0, 1, 0]])
    c = a + b
    print(c)

    a_np = np.array([[1, 2, 3], [4, 5, 6]])
    b_np = np.array([[1, 0, 0], [0, 1, 0]])
    c_np = a_np + b_np
    print(c_np)


if __name__ == '__main__':
    main()
