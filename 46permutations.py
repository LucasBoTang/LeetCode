class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if not nums:
            return result
        self.recursion(nums, [], result)
        return result

    def recursion(self, nums, permutation, result):
        """
        :type nums: List[int]
        :type target: int
        :type permutation: List[int]
        :type result: List[List[int]]
        """
        if len(nums) == len(permutation):
            result.append(permutation)
        for i in range(0, len(nums)):
            if nums[i] in permutation:
                continue
            self.recursion(nums, permutation+[nums[i]], result)
