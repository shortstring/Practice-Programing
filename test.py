import string

my_input = input("enter a number or a string")
# if my_input.isnumeric():
if my_input in string.digits:
    print("thats a number")
else:
    print("that aint a number")    