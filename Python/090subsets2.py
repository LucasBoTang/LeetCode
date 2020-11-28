class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        nums.sort()
        self.dfs([], nums, result)

        return result


    def dfs(self, cur, nums, result):
        """
        :type cur: List[int]
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            result

        for i in range(len(nums)):
            new = cur + [nums[i]]

            if new not in result:
                result.append(new)
                result = self.dfs(new, nums[i+1:], result)

        return result
