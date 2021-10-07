# given a  string of words seperated by spaces ("hello world"),
# randomly scramble the internal letters of each word while leaving the first and last letters in space
from random import shuffle


def main():
    my_str = "hello to the world"
    print(scramble_string(my_str))


def scramble_string(my_str):
    final_str = ''
    split_str = my_str.split(' ')
    for i, word in enumerate(split_str):
        # print(i, word)
        # first word
        if(i == 0):
            temp = list(word[1:])
            shuffle(temp),
            word = word[0] + ''.join(temp)
            final_str += word
        # last word
        elif(i == len(split_str)-1):
            temp = list(word[:-1])
            shuffle(temp)
            word = ''.join(temp) + word[-1]
            final_str += " " + word
        # other words
        else:
            temp = list(word)
            shuffle(temp),
            word = ''.join(temp)
            final_str += " " + word
    return final_str


main()
