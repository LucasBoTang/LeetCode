# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        while not headA or not headB:
            return None
        lenA = self.getNodelen(headA)
        lenB = self.getNodelen(headB)
        dif = abs(lenA - lenB)
        if lenA > lenB:
            for _ in range(dif):
                headA = headA.next
        else:
            for _ in range(dif):
                headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

    def getNodelen(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        len = 0
        while head:
            len += 1
            head = head.next
        return len
