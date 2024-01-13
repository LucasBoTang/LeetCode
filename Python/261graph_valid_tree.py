class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # tree must contain n - 1 edges
        if len(edges) != n - 1:
            return False
        # init union find
        uf = UnionFind(n)
        # add each edge
        for i, j in edges:
            uf.union(i, j)
            # check cycle
            if uf.is_cycle:
                return False
        # no cycle
        return True


class UnionFind(object):
    def __init__(self, n):
        # init a hash map of parants (as list)
        self.parent = [None] * n
        self.is_cycle = False
    
    def find(self, i):
        # find root node
        root = i
        while self.parent[root] is not None:
            root = self.parent[root]
        # path campact
        while i != root:
            self.parent[i], i = root, self.parent[i]
        return root

    def union(self, i, j):
        # merge i and j as a connected component
        root_i, root_j = self.find(i), self.find(j)
        # i and j has already been connected
        if root_i == root_j:
            self.is_cycle = True
        # merge i and j
        else:
            self.parent[root_i] = root_j
