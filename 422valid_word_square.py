class Solution:
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        n = len(words)
        for i in range(n):
            word1 = words[i]
            word2 = ''
            for j in range(n):
                if i < len(words[j]):
                    word2 += words[j][i]
            if word1 != word2:
                return False
        return True
