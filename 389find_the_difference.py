class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(26):
            if t.count(letters[i]) > s.count(letters[i]):
                return letters[i]
