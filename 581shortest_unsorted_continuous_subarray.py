class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sorted_nums = sorted(nums)
        start = 0
        end = len(nums) - 1

        while start <= end and nums[start] == sorted_nums[start]:
            start += 1

        while end >= start and nums[end] == sorted_nums[end]:
            end -= 1

        return end - start + 1
