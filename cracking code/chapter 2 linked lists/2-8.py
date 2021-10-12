# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A(corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input: A -> B -> C -> D -> E -> C[the same C as earlier]
# Output: C
# Hints:  # 50, #69, #83, #90
def main():
    list_one = LinkedList()
    list_one.head = Node('A')
    list_one.head.next = Node('B')
    list_one.head.next.next = Node('C')
    list_one.head.next.next.next = Node('D')
    list_one.head.next.next.next.next = Node('E')
    list_one.head.next.next.next.next.next = list_one.head.next.next.next
    print("Loop found and removed at: " + str(list_one.detect_remove_loop()))
    list_one.print_list()


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return self.data


class LinkedList():
    def __init__(self):
        # Head of list
        self.head = None

    def print_list(self):
        if not(self.head):
            return None
        print(self.head.data, end=" -> ")
        self.print_list_r(self.head.next)
        print()

    def print_list_r(self, head):
        if head == None:
            print()
            return None
        print(head.data, end=" -> ")
        return self.print_list_r(head.next)

    def detect_remove_loop(self):
        slow_ptr = self.head.next
        fast_ptr = self.head.next.next
        while fast_ptr and slow_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            # there is a loop
            if slow_ptr == fast_ptr:
                # figure out where
                slow_ptr = self.head
                while slow_ptr.next != fast_ptr.next:
                    slow_ptr = slow_ptr.next
                    fast_ptr = fast_ptr.next
                fast_ptr.next = None
                return slow_ptr


main()
