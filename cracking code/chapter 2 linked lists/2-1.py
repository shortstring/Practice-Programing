# Remove Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
# Hints: #9, #40


def remove_dupes_r(my_list):
    return my_list


def main():
    list = LinkedList()
    list.head = Node(10)
    list.head.next = Node(3)
    list.head.next.next = Node(11)
    list.head.next.next.next = Node(3)
    list.head.next.next.next.next = Node(10)
    list.head.next.next.next.next.next = Node(10)
    list.head.next.next.next.next.next.next = Node(3)
    list.head.next.next.next.next.next.next.next = Node(3)
    list.head.next.next.next.next.next.next.next.next = Node(3)
    print('before removal')
    list.print_list()

    list.remove_dupes()

    print('after removal')
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

    def remove_dupes(self):
        if not(self.head):
            return 0
        used = []
        self.remove_dupes_r(self.head, used)

    def remove_dupes_r(self, head, used):
        if not(head):
            return None
        if head.data in used:
            if(head.next):
                head = head.next
                return self.remove_dupes_r(head, used)
            else:
                head = None
                return None
        else:
            used.append(head.data)
        if(head):
            head.next = self.remove_dupes_r(head.next, used)
            return head
        return None

    def print_list(self):
        if not(self.head):
            return None
        self.print_list_r(self.head)

    def print_list_r(self, head):
        if not(head):
            return None
        print(head.data, end=" -> ")
        self.print_list_r(head.next)


main()
