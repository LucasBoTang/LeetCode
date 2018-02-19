class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        j, k = 0, 0
        for i in range(len(s)):
            if s[i] == " " and j != 0:
                k = j
                j = 0
            elif s[i] != " ":
                j += 1
        if j == 0:
            return k
        else:
            return j
