class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        max_len = 0
        start = 0
        chars = {}

        for i in range(len(s)):
            char = s[i]

            if char in chars and start <= chars[char]:
                max_len = max(max_len, i-start)
                start = chars[char] + 1
            chars[char] = i

        max_len = max(max_len, len(s)-start)
        return max_len
