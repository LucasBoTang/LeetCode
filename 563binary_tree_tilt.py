# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        root_sum, root_tilt = self.getSumAndTilt(root)
        return root_tilt

    def getSumAndTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int, int
        """
        if not root:
            return 0, 0
        left_sum, left_tilt = self.getSumAndTilt(root.left)
        right_sum, right_tilt = self.getSumAndTilt(root.right)
        return root.val + left_sum + right_sum, abs(left_sum - right_sum) + left_tilt + right_tilt
