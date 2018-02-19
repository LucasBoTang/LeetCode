class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            cmn = strs[0]
            for i in range(1, len(strs)):
                cur = strs[i]
                j = 0
                while j < len(cmn) and j < len(cur):
                    if cmn[j] == cur[j]:
                        j = j + 1
                    else:
                        break
                cmn = cmn[:j]
            return cmn
