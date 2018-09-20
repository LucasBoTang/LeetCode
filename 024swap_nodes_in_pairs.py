# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode('i')
        cur = dummy.next = head
        prev = dummy

        while cur:

            if not cur.next:
                break

            temp, cur.next = cur.next, cur.next.next
            prev.next, temp.next = temp, cur
            prev, cur = cur, cur.next

        return dummy.next
