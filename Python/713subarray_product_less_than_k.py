class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # no production
        if k <= 1:
            return 0
        # init count
        cnt = 0
        # init production
        prod = 1
        # start pointer
        start = 0
        # iterate end pointer
        for end in range(len(nums)):
            # update production
            prod *= nums[end]
            # if greater than k
            while prod >= k:
                # move start pointer
                prod /= nums[start]
                start += 1
            # update count
            cnt += end - start + 1
        return cnt

