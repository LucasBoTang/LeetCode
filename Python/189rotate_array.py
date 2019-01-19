class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        while k > n:
            k %= n
        nums[:] = nums[n - k:] + nums[:n - k]
