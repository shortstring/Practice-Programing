# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# lnput:the node c from the linked lista->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f
# Hints:#72

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

    # wrapper to delete the middle node form a LLL, 1 == error 0 == success
    def delete_middle_node(self):
        # need at least 3 nodes to perform delete
        if not self.head or not self.head.next or not self.head.next.next:
            return None
        self.delete_middle_node_r(self.head)
    # recursivley delete a middle node

    def delete_middle_node_r(self, head):
        if not head:
            return None
        if head.next and not head.next.next:
            return head.next
        head.next = self.delete_middle_node_r(head.next)
        return head


# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# lnput:the node c from the linked lista->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f

def main():
    list = LinkedList()
    list.head = Node('a')
    list.head.next = Node('b')
    list.head.next.next = Node('c')
    list.head.next.next.next = Node('d')
    list.head.next.next.next.next = Node('e')
    list.head.next.next.next.next.next = Node('f')
    print('before')
    list.print_list()

    list.delete_middle_node()
    print('after')
    list.print_list()

    list.delete_middle_node()
    print('after')
    list.print_list()

    list.delete_middle_node()
    print('after')
    list.print_list()

    list.delete_middle_node()
    print('after')
    list.print_list()

    list.delete_middle_node()
    print('after')
    list.print_list()


main()
