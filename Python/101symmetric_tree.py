# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # empty tree
        if not root:
            return True
        # dfs
        return self.isSym(root.left, root.right)

    def isSym(self, left, right):
        # base case
        if not left and not right:
            # leaf node
            return True
        if not left or not right or left.val != right.val:
            # asymetric children
            return False
        # recursion case
        outer = self.isSym(left.left, right.right)
        inner = self.isSym(left.right, right.left)
        return outer and inner
