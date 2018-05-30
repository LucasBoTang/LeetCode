# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        result = TreeNode(None)
        self.getAddition(root, 0, result)
        return result



    def getAddition(self, root, add, new):
        """
        :type root: TreeNode
        :type add: int
        :type new: TreeNode
        :rtype: int
        """

        if not root:
            return add

        if root.right:
            new.right = TreeNode(None)
            add = self.getAddition(root.right, add, new.right)

        add += root.val
        new.val = add

        if root.left:
            new.left = TreeNode(None)
            add = self.getAddition(root.left, add, new.left)

        return add
