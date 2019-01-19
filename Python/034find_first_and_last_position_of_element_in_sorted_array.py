class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return (self.searchLeft(nums, 0, mid, target), self.searchRight(nums, mid, len(nums)-1, target))

        return [-1, -1]


    def searchLeft(self, nums, start, end, target):
        """
        :type nums: List[int]
        :type start: int
        :type end: int
        :type target: int
        :rtype: int
        """

        while start <= end:

            if nums[start] == target:
                return start

            mid = start + (end - start) // 2

            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return end + 1


    def searchRight(self, nums, start, end, target):
        """
        :type nums: List[int]
        :type start: int
        :type end: int
        :type target: int
        :rtype: int
        """

        while start <= end:

            if nums[end] == target:
                return end

            mid = start + (end - start) // 2

            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return start - 1
