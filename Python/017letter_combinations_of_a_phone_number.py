class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        result = []
        if not digits:
            return result

        maps = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = self.dfs(digits, '', maps, result)
        return result



    def dfs(self, digits, letters, maps, result):
        """
        :type digits: str
        :type letters: str
        :type maps: dict
        :rtype: List[str]
        """

        if not digits:
            result.append(letters)
            return result

        for letter in maps[digits[0]]:
            result = self.dfs(digits[1:], letters+letter, maps, result)
        return result
