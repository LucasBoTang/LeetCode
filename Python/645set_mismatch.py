class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        duplication = sum(nums) - sum(set(nums))
        missing = n * (n + 1) // 2 - sum(set(nums))
        return [duplication, missing]
