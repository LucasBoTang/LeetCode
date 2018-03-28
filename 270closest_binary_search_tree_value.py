# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        diff = float('inf')
        while root:
            if abs(root.val - target) < diff:
                close, diff = root.val, abs(root.val - target)
            if target < root.val:
                root = root.left
            elif target > root.val:
                root = root.right
            else:
                return root.val
        return close
