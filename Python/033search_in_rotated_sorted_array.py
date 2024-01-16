class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # init pointers
        start, end = 0, len(nums) - 1
        # binary search
        while start <= end:
            # mid pointer
            mid = start + (end - start) // 2
            # find target
            if nums[mid] == target:
                return mid
            # left is sorted
            if nums[mid] >= nums[start]:
                # keep left
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                # keep right
                else:
                    start = mid + 1
            # right is sorted
            else:
                # keep right
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                # keep left
                else:
                    end = mid - 1
        # cannot find target
        return -1
