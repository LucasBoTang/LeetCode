class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        while not s or not p or len(s) < len(p):
            return result
        p_hash, s_hash = {}, {}
        plen, slen = len(p),len(s)
        for i in range(plen):
            p_hash[p[i]] = p_hash.get(p[i], 0) + 1
            s_hash[s[i]] = s_hash.get(s[i], 0) + 1
        for i in range(slen - plen):
            if p_hash == s_hash:
                result.append(i)
            s_hash[s[i]] -= 1
            s_hash[s[i + plen]] = s_hash.get(s[i + plen], 0) + 1
            if s_hash[s[i]] == 0:
                del s_hash[s[i]]
        if p_hash == s_hash:
                result.append(slen - plen)
        return result
