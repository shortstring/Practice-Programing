# 2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2).That is , 617 + 295.
# Output: 2 -> 1 -> 9. That is , 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# lnput: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is , 617 + 295.
# Output: 9 -> 1 -> 2. That is , 912.
# Hints:  # 7, #30, #71, #95, #109
def main():
    print('one')
    list_one = LinkedList()
    list_one.head = Node(6)
    list_one.head.next = Node(1)
    list_one.head.next.next = Node(7)
    list_one.head.next.next.next = Node(4)
    list_one.print_list()

    print('two')
    list_two = LinkedList()
    list_two.head = Node(2)
    list_two.head.next = Node(9)
    list_two.head.next.next = Node(5)
    list_two.head.next.next.next = Node(5)
    list_two.head.next.next.next.next = Node(5)
    list_two.print_list()

    print('three')
    list_three = LinkedList()
    list_three.add_lists(list_one.head, list_two.head)
    list_three.print_list()


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        # Head of list
        self.head = None

    def print_list(self):
        if not(self.head):
            return None
        self.print_list_r(self.head)
        print('')

    def print_list_r(self, head):
        if not(head):
            return None
        print(head.data, end=" -> ")
        return self.print_list_r(head.next)

    def add_lists(self, head_one, head_two):
        if not(head_one) or not(head_two):
            return None
        self.head = self.add_lists_r(head_one, head_two, self.head)
        return self.head

    def add_lists_r(self, head_one, head_two, head_three):
        # both none
        if not(head_one) and not(head_two):
            return None
        # both next
        elif head_one and head_two:
            head_three = Node(head_one.data + head_two.data)
            head_three.next = self.add_lists_r(
                head_one.next, head_two.next, head_three.next)
        # had one longer
        elif head_one and not head_two:
            head_three = Node(head_one.data)
            head_three.next = self.add_lists_r(
                head_one.next, head_two, head_three)
            return head_one
        # head two longer
        elif head_two and not head_one:
            head_three = Node(head_two.data)
            head_three.next = self.add_lists_r(
                head_one, head_two.next, head_three)
            return head_two
        #  both next
        else:
            head_three = self.add_lists_r(
                head_one.next, head_two.next, head_three.next)
        return head_three


main()
