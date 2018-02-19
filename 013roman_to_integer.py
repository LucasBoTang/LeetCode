class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ronu_dict = {'M': 1000,
                     'D': 500 ,
                     'C': 100,
                     'L': 50,
                     'X': 10,
                     'V': 5,
                     'I': 1}
        result = 0
        for i in range(0, len(s) - 1):
            if ronu_dict[s[i]] < ronu_dict[s[i+1]]:
                result -= ronu_dict[s[i]]
            else:
                result += ronu_dict[s[i]]
        return result + ronu_dict[s[-1]]
