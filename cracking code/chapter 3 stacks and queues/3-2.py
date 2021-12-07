my_stack = []
my_stack.append(5)
my_stack.append(5)
my_stack.append(3)
my_stack.append(6)
my_stack.append(2)
my_stack.append(10)

print(my_stack)

def min(stack):
    min = 1000000
    while(stack):
        stack = stack.next   
        return min

print(min(my_stack))
print(my_stack)
