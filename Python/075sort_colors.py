class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        red, white, blue = 0, 0, 0

        for c in nums:
            if c == 0:
                red += 1
            elif c == 1:
                white += 1
            elif c == 2:
                blue += 1

        for i in range(red):
            nums[i] = 0
        for i in range(red, red+white):
            nums[i] = 1
        for i in range(red+white, red+white+blue):
            nums[i] = 2
