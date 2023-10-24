# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # init dummy listnode for the sum
        cur = dummy = ListNode(None)
        # init carry
        carry = 0
        while l1 or l2:
            # sum together
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next
            # carry           
            carry, sum_val = divmod(sum_val, 10)
            # append linked list
            cur.next = ListNode(val=sum_val)
            cur = cur.next
        # carry for the last digit
        if carry:
            cur.next = ListNode(val=carry)
        return dummy.next
            
