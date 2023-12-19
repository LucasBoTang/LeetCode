class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        substr = set()
        for char in s:
            if char in substr:
                cnt += 1
                substr = set()
            substr.add(char)
        cnt += 1
        return cnt
