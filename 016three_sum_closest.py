class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        result = None
        min_diff = float('inf')
        nums.sort()

        for i in range(len(nums)-2):

            if i and nums[i-1] == nums[i]:
                continue
            start, end = i + 1, len(nums) - 1

            while start < end:
                three_sum = nums[i] + nums[start] + nums[end]
                diff = three_sum - target

                if abs(diff) < abs(min_diff):
                    min_diff = diff
                    result = three_sum

                if diff < 0:
                    start += 1
                elif diff > 0:
                    end -= 1
                else:
                    return result

        return result
