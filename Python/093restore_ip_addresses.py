class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = []
        self.dfs([], s)
        return self.result

    def dfs(self, cur, remain):
        """
        :type cur: List[str]
        :type remain: str
        :rtype: void
        """
        for i in range(1,min(4,len(remain))+1):
            seg = remain[:i]
            if (seg == '0' or seg[0] != '0') and int(seg) < 256:
                cur.append(seg)
                if len(cur) == 4 and not remain[i:]:
                    self.result.append('.'.join(cur))
                elif len(cur) < 4 and remain[i:]:
                    self.dfs(cur, remain[i:])
                cur.pop()
