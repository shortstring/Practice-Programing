# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.
# Hints:  # 17, #74, #702

def zero_matrix(matrix):
    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if num == 0:
                return zero_found(matrix, j, i)
    return matrix


def zero_found(matrix, index, my_row):
    for i, row in enumerate(matrix):
        if i == my_row:
            for z, j in enumerate(row):
                row[z] = 0
        row[index] = 0
    return matrix


def main():
    my_matrix = [[1, 2, 3], [4, 5, 6], [7, 0, 9]]
    my_matrix = zero_matrix(my_matrix)
    print(my_matrix)


main()
