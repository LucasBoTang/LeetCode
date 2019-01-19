class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        cur_sum = max_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            cur_sum = cur_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, cur_sum)

        return max_sum / k
