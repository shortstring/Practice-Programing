# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
# Hints:#92, #110


# the string aabcccccaaa would become a2blc5a3
def compress_string(my_str):
    my_dict = dict()
    new_str = ""
    for i, char in enumerate(my_str):
        if not(char in my_dict):
            my_dict[char] = 1
        else:
            my_dict[char] += 1
    print(my_dict)
    for i, key in enumerate(my_dict.keys()):
        new_str += key + str(my_dict[key])
    return new_str


def main():
    print(compress_string("aabbcbcdcadaaaaaaaAAAAAAAAaaaaaaaaaaaaaaaaaaaaaaaa"))
    return 0


main()
