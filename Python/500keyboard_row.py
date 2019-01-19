class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        result = []
        for word in words:
            for row in rows:
                if set(word.lower()) <= row:
                    result.append(word)
                    break
        return result
