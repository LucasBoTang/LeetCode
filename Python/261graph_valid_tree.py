class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False

        graph = {i: set() for i in range(n)}
        for j, k in edges:
            graph[j].add(k)
            graph[k].add(j)

        queue = [0]
        hash = {0}

        while queue:
            new_queue = []
            for node in queue:
                for neighbor in graph[node]:
                    if neighbor in hash:
                        continue
                    hash.add(neighbor)
                    new_queue.append(neighbor)
            queue = new_queue

        return len(hash) == n
