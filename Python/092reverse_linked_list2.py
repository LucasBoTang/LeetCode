# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        prev, cur = None, head
        for i in range(1, m):
            prev, cur = cur, cur.next

        left, right = prev, cur

        prev = None
        for i in range(n - m + 1):
            temp, cur.next = cur.next, prev
            prev, cur = cur, temp

        if left:
            left.next = prev
        else:
            head = prev
        right.next = cur

        return head
