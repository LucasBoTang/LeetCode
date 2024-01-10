class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_sum = sum(nums)
        # if the sum is odd, always false
        if nums_sum % 2 :
            return False
        # use dp to find nums_sum // 2
        target = nums_sum //  2
        # init dp table
        dp_table = [[False] * (target + 1) for _ in range(len(nums))]
        dp_table[0][0] = True
        if nums[0] <= target:
            dp_table[0][nums[0]] = True
        # add num by iteration
        for i in range(1, len(nums)):
            n = nums[i]
            # get sum of partition
            for j in range(target+1):
                # update dp table
                dp_table[i][j] =  dp_table[i-1][j]
                # sum less than target
                if j - n >= 0:
                    dp_table[i][j] |= dp_table[i-1][j-n]
        return dp_table[-1][-1]
