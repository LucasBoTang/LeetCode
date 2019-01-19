# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = cur = ListNode('i')
        carry = 0

        while l1 or l2:
            val = 0

            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            val += carry

            carry = val // 10
            cur.next = ListNode(val%10)
            cur = cur.next

        if carry:
            cur.next = ListNode(1)

        return dummy.next
