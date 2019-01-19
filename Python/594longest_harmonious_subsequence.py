class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hash_nums = {}
        for num in nums:
            hash_nums[num] = hash_nums.get(num, 0) + 1

        max_len = 0
        for num in hash_nums:
            if num + 1 in hash_nums:
                cur_len = hash_nums[num] + hash_nums[num+1]
                max_len = max(max_len, cur_len)

        return max_len
