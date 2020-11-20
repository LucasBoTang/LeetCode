# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        axis_dict = {}
        res = []
        if not root:
            return res
        queue = [(0, 0, root)]
        while queue:
            new_queue = []
            for x, y, node in queue:
                axis_dict[x] = axis_dict.get(x, {})
                axis_dict[x][y] = axis_dict[x].get(y, []) + [node.val]
                if node.left:
                    new_queue.append((x-1, y-1, node.left))
                if node.right:
                    new_queue.append((x+1, y-1, node.right))
            queue = new_queue
        for x in sorted(axis_dict.keys()):
            col = []
            for y in sorted(axis_dict[x].keys(), reverse=True):
                col += sorted(axis_dict[x][y])
            res.append(col)
        return res
