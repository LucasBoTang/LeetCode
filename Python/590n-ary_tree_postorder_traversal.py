"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        result = []

        if not root:
            return result

        for child in root.children:
            result += self.postorder(child)
        result.append(root.val)

        return result
