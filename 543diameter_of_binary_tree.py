# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(1+self.findLongestPath(root.left)+1+self.findLongestPath(root.right), \
                   self.diameterOfBinaryTree(root.left), \
                   self.diameterOfBinaryTree(root.right))

    def findLongestPath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        return 1 + max(self.findLongestPath(root.left), self.findLongestPath(root.right))
