class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        nums.sort()
        for i in range(len(nums)):
            result += nums[i] - nums[0]
        return result
