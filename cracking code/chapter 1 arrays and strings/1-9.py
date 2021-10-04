# String Rotation: Assumeyou have a method isSubstringwhich checks if oneword is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring(e.g., "waterbottle" is a rotation of"erbottlewat").
# Hints:  # 34, #88, # 7 04


def is_substring(str1, str2):
    temp = ""  # used to hold rotated str2
    if(len(str1) != len(str2)):
        return False
    for i, char1 in enumerate(str1):
        for j, char2 in enumerate(str2):
            # first char found?
            if(char1 == char2):
                temp = str2[j:len(str2)] + str2[0:j]
                if temp == str1:
                    return True
    return False


def main():
    str1 = "waterbottle"
    str2 = "terbottlewa"
    print(is_substring(str1, str2))
    return 0


main()
