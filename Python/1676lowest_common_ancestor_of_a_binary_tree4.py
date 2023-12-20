# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        """
        :type root: TreeNode
        :type nodes: List[TreeNode]
        """
        return self.recursion(root, nodes)
    
    def recursion(self, root, nodes):
        # base case
        if root is None:
            return None
        if root in nodes:
            return root
        # recursion
        left = self.recursion(root.left, nodes)
        right = self.recursion(root.right, nodes)
        if left and right:
            return root
        else:
            return left or right
