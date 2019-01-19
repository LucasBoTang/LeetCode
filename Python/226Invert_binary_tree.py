# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        while not root:
            return root
        queue = [root]
        while queue:
            new_queue = []
            for node in queue:
                node.left, node.right = node.right, node.left
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return root


'''
# DFS
class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        while not root:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
'''
