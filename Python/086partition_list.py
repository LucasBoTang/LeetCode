# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_l = ListNode('i')
        dummy_r = ListNode('i')
        l, r = dummy_l, dummy_r
        cur = head

        while cur:
            if cur.val < x:
                l.next = cur
                l = l.next
            else:
                r.next = cur
                r = r.next
            cur = cur.next

        r.next = None
        l.next = dummy_r.next

        return dummy_l.next
