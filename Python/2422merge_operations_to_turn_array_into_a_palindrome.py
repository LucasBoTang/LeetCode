class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # init operations count
        num_opt = 0
        # init pointer
        start, end = 0, len(nums) - 1
        # greedy
        while start < end:
            # already same
            if nums[start] == nums[end]:
                # update pointers
                start += 1
                end -= 1
                # no operation
                continue
            # merge first
            if nums[start] < nums[end]:
                # update nums
                nums[start+1] += nums[start]
                # update pointer
                start += 1
            # merge last
            else:
                # update nums
                nums[end-1] += nums[end]
                # update pointer
                end -= 1
            # update count
            num_opt += 1
        return num_opt
