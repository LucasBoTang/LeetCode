class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # init max size
        size = 0
        # init prefix sum
        psum = 0
        # init hash map
        sum_ind = {}
        for i, n in enumerate(nums):
            # update hash map
            if psum not in sum_ind:
                sum_ind[psum] = i
            # get prefix sum
            psum += n
            # sum equals k
            if psum - k in sum_ind:
                size = max(size, i + 1 - sum_ind[psum - k])
        return size
