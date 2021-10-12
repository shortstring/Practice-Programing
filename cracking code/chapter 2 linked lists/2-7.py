# Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node(by reference) as the jth node of the second
# linked list, then they are intersecting.
# Hints:  # 20, #45, #55, #65, #76, #93, #111, #120, #129
def main():
    print('one')
    list_one = LinkedList()
    list_one.head = Node(1)
    list_one.head.next = Node(3)
    list_one.head.next.next = Node(12)
    list_one.head.next.next.next = Node(6)
    list_one.print_list()

    print('two')
    list_two = LinkedList()
    list_two.head = Node(3)
    list_two.head.next = Node(9)
    list_two.head.next.next = Node(32)
    list_two.head.next.next.next = Node(2)
    list_two.head.next.next.next.next = Node(1)
    list_two.print_list()
    print(list_one.is_intersecting(list_one.head, list_two.head))


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

    def is_intersecting(self, list_one, list_two):
        flag_one = False
        flag_two = False
        curr_one = list_one
        curr_two = list_two
        while (curr_one or not flag_one) and (curr_two or not flag_two):
            if curr_one == curr_two:
                return curr_one
            curr_one = curr_one.next
            curr_two = curr_two.next
            if not curr_one and not flag_one:
                curr_one = list_two
                flag_one = True
            if not curr_two and not flag_two:
                curr_two = list_one
                flag_two = True
        return "no intersection"


main()
