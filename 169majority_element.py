class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return sorted(num)[len(num)/2]
        n = len(nums)
        hash = {}
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
        for key, value in hash.items():
            if value > n/2:
                return key
