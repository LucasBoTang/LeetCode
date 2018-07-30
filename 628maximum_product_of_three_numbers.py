class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, max3 = sorted(nums[:3])[::-1]
        min1, min2 = max3, max2

        for num in nums[3:]:

            if num >= max1:
                max1, max2, max3 = num, max1, max2
            elif num >= max2:
                max2, max3 = num, max2
            elif num >= max3:
                max3 = num

            if num <= min1:
                min1, min2 = num, min1
            elif num <= min2:
                min2 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)
