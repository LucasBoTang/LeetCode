class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n < 1:
            return False
        slow = fast = n
        while True:
            slow = self.happyProcess(slow)
            fast = self.happyProcess(self.happyProcess(fast))
            if slow == fast:
                break
        return slow == 1


    def happyProcess(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            result += (n % 10) ** 2
            n //= 10
        return result
