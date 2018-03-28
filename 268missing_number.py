class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        n = len(nums)
        for i in range(n):
            result ^= i ^ nums[i]
        return result ^ n
