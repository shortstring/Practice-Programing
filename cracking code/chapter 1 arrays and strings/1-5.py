# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false
# Hints:#23, #97, #130

def is_one_away(str1, str2):
    # length must be equal, +1 or -1
    if len(str1) != len(str2) and len(str1) != len(str2) + 1 and len(str1) != len(str2) - 1:
        return False
    my_dict = []
    counter = 0  # track differnces
    for i in str1:
        my_dict.append(i)
    for i in str2:
        if i not in my_dict:
            counter += 1
    return counter <= 1


def main():
    str1 = "pale"
    str2 = "ple"
    print(is_one_away(str1,  str2))

    str1 = "pales"
    str2 = "pale"
    print(is_one_away(str1,  str2))

    str1 = "pale"
    str2 = "bale"
    print(is_one_away(str1,  str2))

    str1 = "pale"
    str2 = "bake"
    print(is_one_away(str1,  str2))

    return 0


main()
