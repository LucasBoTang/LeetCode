class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums

        result = []
        for _ in range(r):
            result += [[None] * c]

        temp = []
        for row in nums:
            for num in row:
                temp.append(num)

        k = 0
        for i in range(r):
            for j in range(c):
                result[i][j] = temp[k]
                k += 1

        return result
