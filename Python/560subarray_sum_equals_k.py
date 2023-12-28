class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # init answer
        cnt = 0
        # init prefix sum
        psum = 0
        # init hash map
        sum_cnt = {}
        for n in nums:
            # update hash map
            sum_cnt[psum] = sum_cnt.get(psum, 0) + 1
            # get prefix sum
            psum += n
            # sum equals k
            if psum - k in sum_cnt:
                cnt += sum_cnt[psum - k]
        return cnt
