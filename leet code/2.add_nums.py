# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head3 = self.addTwoNumbers_r(l1, l2, 0)
        return head3
        
    def addTwoNumbers_r(self,head1, head2, remain):
        if not head1 and not head2:
            if remain:
                return ListNode(remain)
            else:
                return None
        if head1 and head2:
            my_val = head1.val + head2.val + remain
            if my_val >= 10:
                my_val -= 10
                remain = 1
            else:
                remain = 0
            head3 = ListNode(my_val)
            head3.next = self.addTwoNumbers_r(head1.next, head2.next, remain)
            return head3
        elif head1 and not head2:
            my_val = head1.val + remain
            if my_val >= 10:
                my_val -= 10
                remain = 1
            else:
                remain = 0
            head3 = ListNode(my_val)
            head3.next = self.addTwoNumbers_r(head1.next, head2, remain)
            return head3
        elif not head1 and head2:
            my_val = head2.val + remain
            if my_val >= 10:
                my_val -= 10
                remain = 1
            else:
                remain = 0
            head3 = ListNode(my_val)
            head3.next = self.addTwoNumbers_r(head1, head2.next, remain)
            return head3

def main():
    sol = Solution() 
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(3)
    print(sol.addTwoNumbers(l1, l2))

main()