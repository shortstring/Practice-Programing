# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"

def replace_space(my_str):
    for i, char in enumerate(my_str):
        if char == ' ':
            my_str = my_str[0:i] + "%20" + my_str[i+1:len(my_str)]
            return replace_space(my_str)
    return my_str


def main():
    my_str = "replace my space"
    print(replace_space(my_str))
    return 0


main()
