# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
# Recursion
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.recursion(root, result)
        return result

    def recursion(self, root, result):
        """
        :type root: TreeNode
        :type result: List[int]
        """
        if root:
            result.append(root.val)
            self.recursion(root.left, result)
            self.recursion(root.right, result)
'''

# iteration
class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root:
            result.append(root.val)
            left = self.preorderTraversal(root.left)
            right = self.preorderTraversal(root.right)
            result += left + right
            return result
        return []
