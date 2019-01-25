class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reach = 0
        dest = len(nums)
        for pos in range(dest):
            if reach < pos:
                return False
            reach = max(reach, pos+nums[pos])
        return True
