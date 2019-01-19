class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        cur_len = cur_max = 1
        cur_num = nums[0]

        for num in nums[1:]:
            if num > cur_num:
                cur_len += 1
                cur_max = max(cur_max, cur_len)
            else:
                cur_len = 1
            cur_num = num

        return cur_max
