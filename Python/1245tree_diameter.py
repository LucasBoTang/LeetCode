class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # creat graph
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # get longest chain and path from dfs
        max_chain, max_path = self.dfs(0, -1, graph)
        return max_path

    def dfs(self, root, parent, graph):
        # init
        max_chain, max_path = 0, 0
        max_child_chain, second_child_chain = 0, 0
        # get neighbors as child node
        for v in graph[root]:
            # do not go back
            if v == parent:
                continue
            # get child chain and path from dfs
            child_chain, child_path = self.dfs(v, root, graph)
            child_chain += 1
            # longest chain and path
            max_chain = max(max_chain, child_chain)
            max_path = max(max_path, child_path)
            # longest and second longest child chain
            sorted_chains = sorted([max_child_chain, second_child_chain, child_chain])
            _, second_child_chain, max_child_chain = sorted_chains
        # get longest path
        max_path = max(max_path, max_child_chain + second_child_chain)
        return max_chain, max_path
