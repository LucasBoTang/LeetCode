class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for ind, num in enumerate(nums):
            if target - num in nums_dict:
                return nums_dict[target - num], ind
            nums_dict[num] = ind
