class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        while not s:
            return result
        for i in range(len(s) - 1):
            if s[i] != ' ' and s[i + 1] == ' ':
                result += 1
        if s[-1] != ' ':
            result += 1
        return result

    # return len(s.split())
