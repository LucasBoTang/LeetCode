# Definition for singly-linked list.
# class v:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head:
            return head

        dummy = ListNode('i')
        dummy.next = head

        period = 1
        cur = head
        while cur.next:
            cur = cur.next
            period += 1
        tail = cur

        if k % period == 0:
            return dummy.next

        prev = dummy
        cur = head
        for _ in range(period-k%period):
            prev = prev.next
            cur = cur.next
        prev.next = None
        dummy.next = cur
        tail.next = head

        return dummy.next
