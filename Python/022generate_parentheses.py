class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # init result
        res = []
        # dfs
        self.dfs("", 0, 0, n, res)
        return res

    def dfs(self, solution, num_left, num_right, n, res):
        # base case: find a combination
        if num_left == n and num_right == n:
            res.append(solution)
            return
        # recursion case:
        if num_left < n:
            # add left parenthesis
            self.dfs(solution+"(", num_left+1, num_right, n, res)
        if num_left > num_right:
            # add righht parenthesis
            self.dfs(solution+")", num_left, num_right+1, n, res)
