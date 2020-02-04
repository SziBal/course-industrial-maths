from source.matrix import Matrix


def main():
    a = Matrix([[1, 2, 3], [4, 5, 6]])
    b = Matrix([[1, 0, 0], [0, 1, 0]])
    c = a + b
    print(a)
    print(b)
    print(c)


if __name__ == '__main__':
    main()
