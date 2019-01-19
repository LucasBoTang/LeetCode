class Solution:
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        for i in range(len(s) - 1):
            if s[i:i+2] == '++':
                cur = s[:i] + '--' + s[i+2:]
                result.append(cur)
        return result
