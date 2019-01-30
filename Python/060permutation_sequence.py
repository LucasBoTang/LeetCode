class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        nums = [i + 1 for i in range(n)]
        result = ''

        while n:
            period = self.calFac(n-1)
            ind = (k - 1) // period
            result += str(nums[ind])
            nums.pop(ind)
            k %= period
            n -= 1

        return result
