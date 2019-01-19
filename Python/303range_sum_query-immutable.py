class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = [0]
        while not nums:
            return None
        for num in nums:
            self.array.append(self.array[-1] + num)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.array[j + 1] - self.array[i]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
