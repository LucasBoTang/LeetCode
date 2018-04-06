class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur = float('inf')
        letter = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(26):
            if s.count(letter[i]) == 1:
                cur = min(cur, s.find(letter[i]))
        if cur == float('inf'):
            return -1
        else:
            return cur
