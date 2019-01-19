"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = [root]
        result = [[root.val]]

        while queue:
            row = []
            new_queue = []
            for node in queue:
                for child in node.children:
                    row.append(child.val)
                    new_queue.append(child)
            result.append(row)
            queue = new_queue

        return result[:-1]
