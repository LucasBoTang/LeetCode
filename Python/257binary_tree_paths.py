# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        if not root:
            return result
        if not root.left and not root.right:
            result.append(str(root.val))
            return result
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        for path in left:
            result.append(str(root.val) + '->' + path)
        for path in right:
            result.append(str(root.val) + '->' + path)
        return result
