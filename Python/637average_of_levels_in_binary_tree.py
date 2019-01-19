# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        if not root:
            return []

        result = []
        level = [root]

        while level:
            new_level = []
            total = 0

            for node in level:
                total += node.val
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)

            result.append(total/len(level))
            level = new_level

        return result
