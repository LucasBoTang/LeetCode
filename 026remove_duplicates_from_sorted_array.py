class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        lennum = len(nums)
        if lennum == 0:
            return 0
        for j in range(lennum):
            if nums[i] != nums[j] and nums[i] < nums[j]:
                nums[i+1] = nums[j]
                i += 1
        return i+1
