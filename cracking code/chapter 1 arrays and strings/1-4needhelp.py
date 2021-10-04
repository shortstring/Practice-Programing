# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# 1.5
# 1.6
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)
# Hints: #106, #121, #134, #136

# this function is useless as it will always return true. There is not limitation on the definition of what
# qualifies as a palindrome, so any string is considered a permuation of a palindrome of itself.
def is_permutation_of_palindrome(my_str):
    my_val1 = 0  # ascii sum
    my_val2 = 0
    my_str = my_str.lower()
    # sum ascii
    for i in my_str:
        my_val1 += ord(i)
    # reverse
    my_str = my_str[::-1]
    # sum ascii .. again?
    for i in my_str:
        my_val2 += ord(i)
    return my_val1 == my_val2


def main():
    my_str = "Tact Coa"
    print(is_permutation_of_palindrome(my_str))


main()
