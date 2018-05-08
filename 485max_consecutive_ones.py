class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = cur = 0
        for num in nums:
            if num:
                cur += 1
                result = max(cur, result)
            else:
                cur = 0
        return result
