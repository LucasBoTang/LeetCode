class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.addParenthesis('', 0, 0, n, result)
        return result


    def addParenthesis(self, solution, left, right, n, result):
        """
        :type solution: str
        :type n: int
        :type left: int
        :type right: int
        :rtype: List[str]
        """

        if right + left == 2 * n:
            result.append(solution)
            return

        if left < n:
            self.addParenthesis(solution+'(', left+1, right, n, result)
        if right < left:
            self.addParenthesis(solution+')', left, right+1, n, result)
