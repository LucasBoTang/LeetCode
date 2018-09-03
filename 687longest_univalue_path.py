# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self.univalueChildPath(root)[0]



    def univalueChildPath(self, root):
        """
        :type root: TreeNode
        :rtype: int, int
        """

        if not root:
            return 0, 0
        left_len, right_len = 0, 0
        left_max, right_max = 0, 0

        if root.left:
            left_max, left_temp = self.univalueChildPath(root.left)
            if root.val == root.left.val:
                left_len = left_temp + 1

        if root.right:
            right_max, right_temp = self.univalueChildPath(root.right)
            if root.val == root.right.val:
                right_len += right_temp + 1

        return max(left_len + right_len, left_max, right_max), max(left_len, right_len)
        
