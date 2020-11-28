# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy, dummy.next = ListNode(0), head
        prev = dummy
        while prev is not None:
            prev = self.reverseNextKNodes(prev, k)
        return dummy.next

    def reverseNextKNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # find kth node
        cur, first_node = head, head.next
        for _ in range(k):
            cur = cur.next
            while cur is None:
                return None
        kth_node = cur
        kth_next = cur.next
        # reverse
        prev, cur = head, head.next
        while cur != kth_next:
            temp, cur.next = cur.next, prev
            prev, cur = cur, temp
        head.next, first_node.next = kth_node, kth_next
        return first_node
