class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        lar = -float('inf')
        for num in nums:
            cur = max(num, cur+num)
            lar = max(cur, lar)
        return lar
