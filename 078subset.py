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

    def recursion(self, sub, nums, startIndex, result):
        """
        :type sub: List[List[int]]
        :type nums: List[int]
        :type startIndex: int
        :type result: List[List[int]]
        """
        result.append(sub)
        for i in range(startIndex, len(nums)):
            self.recursion(sub+[nums[i]], nums, i+1, result)
