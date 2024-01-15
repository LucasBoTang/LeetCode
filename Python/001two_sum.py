 class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # init hash map
        nums_dict = {}
        # each element and indice
        for i, n in enumerate(nums):
            # two sum equals to target
            if target - n in nums_dict:
                # index
                return nums_dict[target - n], i
            # record element and indice
            nums_dict[n] = i
