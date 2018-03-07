class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums = sorted(nums)
        result = []
        self.recursion([], nums, 0, result)
        return result

    def recursion(self, sub, nums, startindex, result):
        """
        :type sub: List[int]
        :type nums: List[int]
        :type startindex: int
        :type result: List[List[int]]
        """
        result.append(sub)
        for i in range(startindex, len(nums)):
            self.recursion(sub+[nums[i]], nums, i+1, result)
