class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        tot = 1
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                if i != num // i:
                    tot += i + num // i
                else:
                    tot +=  i
            if tot > num:
                return False
        return tot == num
