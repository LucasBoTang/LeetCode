class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = [0 for i in range(len(s)+1)]

        if s[0] != '0':
            table[0] = 1
        else:
            table[0] = 0

        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                table[i] += table[i-1]
            if i > 1 and '10' <= s[i-2:i] <= '26':
                table[i] += table[i-2]

        return table[-1]
        
