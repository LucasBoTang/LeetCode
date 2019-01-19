class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s) // 2 + 1):
            pattern = s[:i]
            times = len(s) // i
            if pattern * times == s:
                return True
        return False
