# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        branches, nodes = [root], []
        while branches:
            nodes.insert(0, [branch.val for branch in branches])
            subbranches = []
            for branch in branches:
                if branch.left:
                    subbranches.append(branch.left)
                if branch.right:
                    subbranches.append(branch.right)
            branches = subbranches
        return nodes
