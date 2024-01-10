class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sum = sum(nums)
        # if the sum is odd, always false
        if nums_sum % 2:
            return False
        # use dp to find nums_sum // 2
        target = nums_sum //  2
        # init dp table
        dp_table = [True] + [False] * target
        # add num by iteration
        for n in nums:
            # get sum of partition
            for t in range(target, -1, -1): # reversed order to avoid duplication
                # sum less than target
                if t - n >= 0:
                    # update dp table
                    dp_table[t] |= dp_table[t-n]
        return dp_table[-1]
