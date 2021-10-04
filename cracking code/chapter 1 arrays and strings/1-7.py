# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
# Hints: #51, # 100

# 1 2 3
# 4 5 6
# 7 8 9

# clockwise
# 7 4 1
# 8 5 2
# 9 6 3

# rotate clockwise
def rotate_matrix_cw(my_img):
    new_img = [[], [], []]
    for i, row in enumerate(my_img):
        for index, char in enumerate(row):
            new_img[index].insert(0, char)
    return new_img


# 1 2 3
# 4 5 6
# 7 8 9

# counter-clockwise
# 3 6 9
# 2 5 8
# 1 4 7

# rotate counter-clockwise
def rotate_matrix_ccw(my_img):
    new_img = [[], [], []]
    for i, row in enumerate(my_img):
        for index, char in enumerate(row):
            new_img[len(my_img) - 1 - index].append(char)
    return new_img


def main():
    my_img = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Before")
    print_matrix(my_img)

    my_img = rotate_matrix_cw(my_img)
    print("After cw rotate")
    print_matrix(my_img)

    my_img = rotate_matrix_cw(my_img)
    print("After cw rotate")
    print_matrix(my_img)

    my_img = rotate_matrix_ccw(my_img)
    print("After ccw rotate")
    print_matrix(my_img)

    my_img = rotate_matrix_ccw(my_img)
    print("After ccw rotate")
    print_matrix(my_img)
    return 0


def print_matrix(my_img):
    print(my_img[0])
    print(my_img[1])
    print(my_img[2])
    return 0


main()
