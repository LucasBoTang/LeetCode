class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # init results
        product = [1] * len(nums)
        # init prefix & postfix
        prefix, postfix = 1, 1
        # prefix product
        for i in range(len(nums)):
            product[i] *= prefix
            prefix *= nums[i]
        # postfix product
        for i in range(len(nums)-1, -1, -1):
            product[i] *= postfix
            postfix *= nums[i]
        return product
