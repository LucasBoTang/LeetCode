# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        while not root:
            return 0
        return self.findPath(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def findPath(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        result = 0
        while not root:
            return result
        if root.val == sum:
            result += 1
        result += self.findPath(root.left, sum - root.val) + self.findPath(root.right, sum - root.val)
        return result
        
