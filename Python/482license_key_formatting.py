class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-', '')
        S_lst = list(S)[::-1]
        i = K
        while i < len(S_lst):
            S_lst.insert(i, '-')
            i += K + 1
        return ''.join(S_lst)[::-1]
