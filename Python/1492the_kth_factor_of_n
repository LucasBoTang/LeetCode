class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        cnt = 0
        # from 1 to n/2
        for i in range(1, n//2+1):
            if n % i == 0:
                cnt += 1
            if cnt == k:
                return i
        # n itself
        if cnt + 1 == k:
            return n
        return -1
