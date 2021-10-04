# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
# Hints:  # 44, #117, #732

# with a hashtable/dict
def is_unique(my_str):
    my_dict = []
    if len(my_str) <= 1:
        return True
    for i, char in enumerate(my_str):
        if char in my_dict:
            return False
        else:
            my_dict.append(char)
    return True
    #     print(i, char)


def test_function():
    my_str = "dogertyuiop"
    print(is_unique(my_str))


def main():
    test_function()


main()
