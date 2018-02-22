# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.isSym(root.left, root.right)
        return True

    def isSym(self, left, right):
        """
        :type left: TreeNode
        :type right: TreeNode
        :rtype: bool
        """
        if right == None and left == None:
            return True
        if right and left and left.val == right.val:
            return self.isSym(left.left, right.right) and self.isSym(left.right, right.left)
        return False
