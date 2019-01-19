class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []
        nums.sort()

        for i in range(len(nums)-2):
            if i and nums[i-1] == nums[i]:
                continue

            for j in range(i+1, len(nums)-2):
                if j != i + 1 and nums[j-1] == nums[j]:
                    continue

                start, end = j + 1, len(nums) - 1

                while start < end:
                    four_sum = nums[i] + nums[j] + nums[start] + nums[end]
                    diff = four_sum - target

                    if diff < 0:
                        start += 1
                    elif diff > 0:
                        end -= 1
                    else:
                        result.append((nums[i], nums[j], nums[start], nums[end]))

                        while start < end and nums[start] == nums[start+1]:
                            start += 1
                        while start < end and nums[end] == nums[end-1]:
                            end -= 1

                        start += 1
                        end -= 1

        return result
