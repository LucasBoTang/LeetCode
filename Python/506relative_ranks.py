class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        rank_map = {}
        for i, score in enumerate(sorted(nums, reverse=True)):
            if i == 0:
                rank_map[score] = 'Gold Medal'
            elif i == 1:
                rank_map[score] = 'Silver Medal'
            elif i == 2:
                rank_map[score] = 'Bronze Medal'
            else:
                rank_map[score] = str(i+1)
        result = []
        for score in nums:
            result.append(rank_map[score])
        return result
