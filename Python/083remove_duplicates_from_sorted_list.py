# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nl = ListNode(-float('inf'))
        cur = nl
        while head:
            if head.val > cur.val:
                cur.next = head
                cur = cur.next
            head = head.next
        cur.next = None
        return nl.next
