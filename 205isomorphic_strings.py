class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash = {}
        tmap = []
        for i in range(len(s)):
            if s[i] not in hash:
                hash[s[i]] = t[i]
                tmap.append(t[i])
            elif hash[s[i]] != t[i] :
                return False
        if len(tmap) > len(set(tmap)):
            return False
        return True
