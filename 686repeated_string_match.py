class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        t = (len(B) - 1) // len(A) + 1

        if B in A * t:
            return t

        if B in A * (t + 1):
            return t + 1

        return -1
