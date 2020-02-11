from lectures.lecture_1.matrix import Matrix
import numpy as np
import matplotlib.pyplot as plt


def matrices_in_numpy():
    mtx = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print('mtx =', mtx)
    print('mtx.shape =', mtx.shape)
    print('mtx[1,2] =', mtx[1, 2])

    mtx_2 = np.array([[0, 1, -1], [1, -1, 0], [-1, 0, 1]])
    print('mtx:\n', mtx)
    print('mtx_2:\n', mtx_2)
    print('mtx + mtx_2:\n', mtx + mtx_2)
    print('mtx * mtx_2:\n', mtx * mtx_2)

    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    print('A=\n', A)
    print('B=\n', B)

    print('A.t: \n', A.T)
    print('A.B=\n', np.dot(A, B))
    # print(np.dot(B, A))
    print('mtx.mtx_2 = \n', np.dot(mtx, mtx_2))
    print('mtx_2.mtx = \n', np.dot(mtx_2, mtx))


def main():
    a = Matrix([[1, 2, 3], [4, 5, 6]])
    b = Matrix([[1, 0, 0], [0, 1, 0]])
    c = a + b
    print(a)
    print(b)
    print(c)
    print('------------------- Matrices in NumPy ------------------------')
    matrices_in_numpy()

    x = np.arange(-3, 3, 0.001)
    plt.plot(x, np.sin(x))
    plt.show()


if __name__ == '__main__':
    main()
