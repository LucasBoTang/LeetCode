# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_diam, max_len = self.dfs(root)
        return max_diam

    # dfs
    def dfs(self, root):
        # base case
        if not root:
            return 0, 0
        # recursion
        max_diam_left, max_len_left = self.dfs(root.left)
        max_diam_right, max_len_right = self.dfs(root.right)
        max_diam = max(max_len_left + max_len_right, 
                       max_diam_left,
                       max_diam_right)
        max_len = 1 + max(max_len_left, max_len_right)
        return max_diam, max_len
