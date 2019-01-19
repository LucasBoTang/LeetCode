# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        sumlist = self.treeSums(root)
        if sum in sumlist:
            return True
        return False

    def treeSums(self, root):
        """
        :type root: TreeNode
        :rtype: list
        """
        if not root:
            return [0]
        if not root.left:
            return [root.val + cur for cur in self.treeSums(root.right)]
        if not root.right:
            return [root.val + cur for cur in self.treeSums(root.left)]
        return [root.val + cur for cur in self.treeSums(root.left)] + [root.val + cur for cur in self.treeSums(root.right)]
