class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ''
        for i in range(0, len(s), 2*k):
            result += s[i:i+k][::-1] + s[i+k:i+2*k]
        return result
