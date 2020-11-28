class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        length = 1
        cnt = 1
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == prev:
                cnt += 1
            else:
                prev = nums[i]
                cnt = 1
            if cnt <= 2:
                nums[length] = nums[i]
                length += 1

        return length
