# Palindrome: Implement a function to check if a linked list is a palindrome.
# Hints:  # 5, #13, #29, #61, #101
# palindromes: same forward as backword
def main():
    print('one')
    list_one = LinkedList()
    list_one.head = Node('c')
    list_one.head.next = Node('i')
    list_one.head.next.next = Node('v')
    list_one.head.next.next.next = Node('i')
    list_one.head.next.next.next.next = Node('c')
    list_one.print_list()
    print(list_one.is_palindrome())


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

    def get_len(self):
        temp = self.head
        n = 0
        while temp:
            n += 1
            temp = temp.next
        return n

    def is_palindrome(self):
        # no letters
        if not self.head:
            return False
        # one letter
        if not self.head.next:
            return False
        # two letters
        if not self.head.next.next:
            if self.head.data == self.head.next.data:
                return True
            else:
                return False
        my_len = self.get_len()
        front = []
        back = []
        front_size = int(my_len/2)
        temp = self.head
        for i in range(front_size):
            front += temp.data
            temp = temp.next
        # length is even
        if my_len % 2:
            # skip middle
            temp = temp.next
        for i in range(front_size):
            back.insert(0, temp.data)
            temp = temp.next
        if front == back:
            return True
        else:
            return False


main()
