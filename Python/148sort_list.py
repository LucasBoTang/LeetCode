# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.mergeSort(head)


    def mergeSort(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # condition
        if not head or not head.next:
            return head
        # recursion
        l, r = self.listSplit(head)
        l = self.mergeSort(l)
        r = self.mergeSort(r)
        # merge
        dummy = ListNode(None)
        cur = dummy
        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = r or l
        return dummy.next


    def listSplit(self, head):
        """
        :type head: ListNode
        :rtype: ListNode, ListNode
        """
        # find median
        mid, slow, fast = head, head, head
        while fast and fast.next:
            mid = slow
            slow = slow.next
            fast = fast.next.next
        # left part
        mid.next = None
        l = head
        # right part
        r = slow
        return r, l
