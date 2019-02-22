# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode('i')
        dummy.next = head

        prev, cur = dummy, head
        duplicate = False

        while cur:
            if cur.next and cur.val == cur.next.val:
                duplicate = True
                prev.next = cur.next
            else:
                if duplicate:
                    prev.next = cur.next
                    duplicate = False
                else:
                    prev = prev.next
            cur = cur.next

        return dummy.next
