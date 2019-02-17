class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs([], 1, n, k)
        return self.result


    def dfs(self, cur, start, n, k):
        """
        :type cur: list
        :type start: int
        :type n: int
        :type k: int
        :rtype: void
        """
        if k == 0:
            self.result.append(cur)
        else:
            for i in range(start, n+1):
                self.dfs(cur+[i], i+1, n, k-1)
