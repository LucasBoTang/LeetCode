class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        count = 0

        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            else:
                if i == 0 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
                count += 1


            if count > 1:
                return False

        return True
