# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        num_lst = self.traverseInOrder(root)
        result = float('inf')
        for i in range(1, len(num_lst)):
            result = min(result, num_lst[i]-num_lst[i-1])
        return result



    def traverseInOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        if root.left:
            result += self.traverseInOrder(root.left)
        result += [root.val]
        if root.right:
            result += self.traverseInOrder(root.right)
        return result
