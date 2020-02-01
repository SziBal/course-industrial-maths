class Matrix:
    def __init__(self, data):
        self.__data = data

    def __add__(self, other):
        # Check compatibility
        are_compatible = True
        if len(self.__data) == len(other.__data):
            for (x, y) in zip(self.__data, other.__data):
                if len(x) != len(y):
                    are_compatible = False
        else:
            are_compatible = False

        # Execute addition
        result = []
        if are_compatible:
            for (row1, row2) in zip(self.__data, other.__data):
                result_row = []
                for (element1, element2) in zip(row1, row2):
                    result_row.append(element1 + element2)
                result.append(result_row)
        else:
            print('The matrices are not compatible')
            exit()
        return Matrix(result)

    def __str__(self):
        return str(self.__data)
