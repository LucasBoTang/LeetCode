class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # init union find
        uf = UnionFind(n)
        # add each edge
        for i, j in edges:
            uf.union(i, j)
        return uf.num_comp
        

class UnionFind(object):
    def __init__(self, n):
        # init a hash map of parants (as list)
        self.parent = [None] * n
        # init number of connected components
        self.num_comp = n
    
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
        if root_i != root_j:
            # merge i and j
            self.parent[root_i] = root_j
            self.num_comp -= 1
