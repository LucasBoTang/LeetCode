class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_lst = s.split()
        r_lst = []
        for word in s_lst:
            r_lst.append(word[::-1])
        return ' '.join(r_lst)
