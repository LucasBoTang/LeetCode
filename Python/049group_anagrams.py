class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anag_dict = collections.defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            anag_dict[key].append(s)
        return anag_dict.values()
