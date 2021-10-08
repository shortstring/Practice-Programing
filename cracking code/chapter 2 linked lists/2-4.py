#  Partition: Write code to partition a linked list around a value x,
# such that all nodes less than x come
# before all nodes greater than or equal to x.
#
# If x is contained within the list, the values of x only need
# to be after the elements less than x (see below).
#
# The partition element x can appear anywhere in the
# "right partition";
#
# it does not need to appear between the left and right partitions.
#
# EXAMPLE
# Input:
# 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
# Output:
# 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
# Hints: #3, #24

def main():
    list = LinkedList()
    list.head = Node(3)
    list.head.next = Node(5)
    list.head.next.next = Node(8)
    list.head.next.next.next = Node(5)
    list.head.next.next.next.next = Node(10)
    list.head.next.next.next.next.next = Node(2)
    list.head.next.next.next.next.next.next = Node(1)

    print('before')
    list.print_list()
    list.partition_list(3)
    print('after')
    list.print_list()
    return 0


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
        self.print_list_r(head.next)

    def partition_list(self, x):
        if not self.head:
            return None

        low_list = LinkedList()
        low_head = None
        low_tail = None

        high_list = LinkedList()
        high_head = None

        head = self.head
        while head:
            if head.data >= x:
                if not high_head:
                    high_head = Node(head.data)
                else:
                    temp = Node(head.data)
                    temp.next = high_head
                    high_head = temp
            else:
                if not low_head:
                    low_head = Node(head.data)
                    low_tail = low_head
                else:
                    temp = Node(head.data)
                    temp.next = low_head
                    low_head = temp
            head = head.next
        if not low_head:
            self.head = high_head
        else:
            low_tail.next = high_head
            self.head = low_head

    # attempt to solve recursivley...
        # gave up and solved iteravely because i dont know how to return the high and low list

    # def partition_list_r(self, head, low_list, high_list, x):
    #     # case 1: not head
    #     if not head:
    #         return None
    #     # case 2: check if head value is  greater/equal than x
    #     elif head.data >= x:
    #         high_list = self.add_to_head(high_list.head, head.data)
    #     # case 3: head < x
    #     else:
    #         low_list = self.add_to_head(low_list.head, head.data)

    # def add_to_head(self, head, to_add):
    #     if(not head):
    #         head = Node(to_add)
    #     else:
    #         temp = Node(to_add)
    #         temp.next = head
    #         head = temp
    #     return head

    # def combine_lists(self, head_one, head_two):
    #     if not head_one or not head_one.next:
    #         return head_two
    #     head_one.next = self.combine_lists(self, head_one.next, head_two)
    #     return head_one


main()
