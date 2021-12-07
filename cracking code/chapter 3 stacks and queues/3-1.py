# 3.1 Three in One: Describe how you could use a single array to implement three stacks.

# Hints:  # 2, #72, #38, #58
    # to implement three stacks into a single array:
        # have an array of three stack ptrs

stack_1 = []
stack_2 = []
stack_3 = []
my_stack_array = [stack_1, stack_2, stack_3]

# Stacks are First In Last Out.. FILO

stack_1.append('A')
stack_1.append('B')
stack_1.append('C')

stack_2.append('A')
stack_2.append('B')
stack_2.append('C')

stack_3.append('A')
stack_3.append('B')
stack_3.append('C')

print(my_stack_array)