# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

def is_permutation(str1, str2):
    value1 = 0
    value2 = 0
    #sum ascii of all chars
    for i in str1:
        value1 += ord(i)
    for i in str2:
        value2 += ord(i)
    # if some of ascii values is equal, then the two strings are permutations of each other.
    if value1 == value2:
        return True
    else:
        return False


def main():
    str1 = "qwertyuiop"
    str2 = "poiuytrewq"
    print(is_permutation(str1, str2))


main()
