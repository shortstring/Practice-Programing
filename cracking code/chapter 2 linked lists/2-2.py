# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
# Hints:  # 8, #25, #41, #67, #126


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

    def print_list_r(self, head):
        if not(head):
            return None
        print(head.data, end=" -> ")
        self.print_list_r(head.next)

    # wrapper, argument is n from the last element
    def n_to_last(self, n):
        if not(self.head):
            return None
        if n == 0:
            return None
        # if n > len(list):return
        return int(self.n_to_last_r(self.head, n))

    # recursive function
    def n_to_last_r(self, head, n):
        if not(head):
            return n - 1
        n = self.n_to_last_r(head.next, n)
        if isinstance(n, str):
            return n
        if n == 0:
            n = head.data
            return str(n)
        return n - 1


def main():
    list = LinkedList()
    list.head = Node(10)
    list.head.next = Node(3)
    list.head.next.next = Node(11)
    list.head.next.next.next = Node(3)
    print(list.n_to_last(1))


main()
