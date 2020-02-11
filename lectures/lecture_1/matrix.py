class Matrix:
    def __init__(self, data=None):
        is_rectangular = check_format(data)
        if is_rectangular:
            self.data = data
            self.rows = len(data)
            self.columns = len(data[0])

    def __str__(self):
        return str(self.data)

    def __add__(self, other):
        result = []
        if self.rows == other.rows and self.columns == other.columns:
            for (row1, row2) in zip(self.data, other.data):
                result_row = []
                for (element1, element2) in zip(row1, row2):
                    result_row.append(element1 + element2)
                result.append(result_row)
        else:
            raise Exception('The matrices are not compatible!')
        return Matrix(result)


def check_format(data):
    if isinstance(data[0], list):
        number_of_columns = len(data[0])
    else:
        raise Exception('You must give an array of arrays!')

    is_rectangular = True
    for row in data:
        is_rectangular = is_rectangular and (len(row) == number_of_columns)

    if not is_rectangular:
        raise Exception('The given data is not a rectangular table!')

    return is_rectangular
