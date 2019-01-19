class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for index, num in enumerate(nums):
            if target - num in nums_dict:
                return [nums_dict[target - num], index]
            nums_dict[num] = index
        return
