# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        min1, min2 = root.val, float('inf')
        queue = [root]

        while queue:
            new_queue = []
            for node in queue:

                if node.left:
                    new_queue.append(node.left)
                    left = node.left.val
                    if left < min1:
                        min1, min2 = left, min1
                    elif left != min1 and left < min2:
                        min2 = left

                if node.right:
                    new_queue.append(node.right)
                    right = node.right.val
                    if right < min1:
                        min1, min2 = right, min1
                    elif right != min1 and right < min2:
                        min2 = right

            queue = new_queue

        if min1 == min2 or min2 == float('inf'):
            return -1
        else:
            return min2
