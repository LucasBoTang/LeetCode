class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        count_ls = [1]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count_ls[-1] += 1
            else:
                count_ls.append(1)

        result = 0
        for i in range(1, len(count_ls)):
            result += min(count_ls[i-1], count_ls[i])

        return result
