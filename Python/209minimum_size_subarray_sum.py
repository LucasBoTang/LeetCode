class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # init prefix sum
        psums = [0]
        for n in nums:
            psums.append(psums[-1] + n)
        # init min size
        size = float("inf")
        for i in range(len(nums)):
            # binary search
            start, end = i, len(nums) - 1
            while start + 1 < end:
                mid = start + (end - start) // 2
                if psums[mid + 1]  - psums[i] >= target:
                    end = mid
                else:
                    start = mid
            # find a subarray
            if psums[start + 1]  - psums[i] >= target:
                size = min(size, start - i + 1)
            elif psums[end + 1]  - psums[i] >= target:
                size = min(size, end - i + 1)
        return size if size != float("inf") else 0
