class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        result = float('inf')
        for i in range(len(words)):
            if word1 == words[i]:
                loc1 = i
            if word2 == words[i]:
                loc2 = i
            try:
                result = min(abs(loc1-loc2), result)
            except:
                continue
        return result
