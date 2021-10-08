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
    list.partition_list(5)
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
        return self.partition_list_r(self.head, x)

    def partition_list_r(self, head, x):
        # case 1: not head
        if not head:
            return None
        # case 2: check if head value is  greater than x
        elif head.data > x:
            if head.next and head.next.data < x:
                temp = head
                head = head.next
                head.next = temp
            # if head < x
            # then if head.next < x
            #   then swap nodes
            # '''
        # case 3: head == x
        elif head.data == x:
            if head.next and head.next.data < x:
                temp = head
                head = head.next
                head.next = temp
        # case 4: head < x
        else:
            pass
        head.next = self.partition_list_r(head.next, x)
        return head


main()
