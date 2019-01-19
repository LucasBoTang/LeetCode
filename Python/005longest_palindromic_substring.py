class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        max_span = 0
        center = 0
        s = '#' + '#'.join(list(s)) + '#'

        for i in range(len(s)):

            if i + max_span >= len(s):
                break

            temp = s[i-max_span:i+max_span+1]
            if temp != temp[::-1]:
                continue
            cur_span = max_span

            while s[i-cur_span] == s[i+cur_span]:
                max_span = cur_span
                center = i
                cur_span += 1

                if i - cur_span < 0 or i + cur_span >= len(s):
                    break

        result = [i for i in s[center-max_span:center+max_span] if i != '#']
        return ''.join(result)
