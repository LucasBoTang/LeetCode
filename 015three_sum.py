class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        nums.sort()

        for i in range(len(nums)-2):

            if i and nums[i-1] == nums[i]:
                continue
            start, end = i + 1, len(nums) - 1

            while start < end:
                tree_sum = nums[i] + nums[start] + nums[end]

                if tree_sum < 0:
                    start += 1
                elif tree_sum > 0:
                    end -= 1
                else:
                    result.append((nums[i], nums[start], nums[end]))

                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1

                    start += 1
                    end -= 1

        return result
