class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, n = 0, len(nums)
        for j in range(n):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        nums[i:] = [0] * (n - i)
