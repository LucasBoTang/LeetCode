# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


    def maxDepth(self, root): # 104maximum_depth_of_binary_tree.py
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return 0
