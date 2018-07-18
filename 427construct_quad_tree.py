"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """

        n = len(grid)
        if not n:
            return None

        if all(all(row) for row in grid):
            return Node(True, True, None, None, None, None)

        if not any(any(row) for row in grid):
            return Node(False, True, None, None, None, None)

        d = n // 2
        topleft = self.construct([row[:d] for row in grid[:d]])
        topright = self.construct([row[d:] for row in grid[:d]])
        bottomleft = self.construct([row[:d] for row in grid[d:]])
        bottomright = self.construct([row[d:] for row in grid[d:]])
        return Node(True, False, topleft, topright, bottomleft, bottomright)
