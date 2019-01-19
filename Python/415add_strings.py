class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        while not num1:
            return num2
        while not num2:
            return num1

        num1, num2 = num1[::-1], num2[::-1]
        if len(num1) > len(num2):
            num2 += '0' * (len(num1) - len(num2))
        else:
            num1 += '0' * (len(num2) - len(num1))

        result, carry = '', 0
        for i in range(len(num1)):
            cur = ord(num1[i]) + ord(num2[i]) - 2 * ord('0') + carry
            result += str(cur % 10)
            carry = cur // 10
        if carry:
            result += '1'

        return result[::-1]
