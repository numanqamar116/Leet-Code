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
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sum = carry + x + y
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy_head.next
