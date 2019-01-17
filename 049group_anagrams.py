class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = collections.defaultdict(list)
        for s in strs:
            key =  "".join(sorted(s))
            result[key].append(s)
        return result.values()
