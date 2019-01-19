class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if not num1 or not num2:
            return '0'

        num1 = num1[::-1]
        num2 = num2[::-1]

        res_lst = [0 for _ in range(len(num1) + len(num2))]
        carry = 0

        for i in range(len(num1)):
            for j in range(len(num2)):

                digit = int(num1[i]) * int(num2[j]) + res_lst[i+j]
                res_lst[i+j] = digit % 10
                carry = digit // 10

                k = 1
                while carry:
                    digit = res_lst[i+j+k] + carry
                    res_lst[i+j+k] = digit % 10
                    carry = digit // 10
                    k += 1

        while len(res_lst) > 1 and res_lst[-1] == 0:
            res_lst = res_lst[:-1]

        return ''.join([str(num) for num in res_lst][::-1])
