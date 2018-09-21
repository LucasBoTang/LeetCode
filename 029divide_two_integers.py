class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        result = []

        sign = 1
        if (dividend < 0) ^ (divisor < 0):
            sign = -1

        if dividend < 0:
            dividend = - dividend
        if divisor < 0:
            divisor = - divisor
        dividend = str(dividend)

        i, length = 0, len(dividend)
        carry = 0

        while i < length:
            num = carry + int(dividend[i])
            carry = 0
            i += 1

            count = 0
            while num >= divisor:
                num -= divisor
                count += 1
            result.append(str(count))
            carry = int(str(num)+'0')

        result = int(''.join(result))
        result *= sign

        if sign > 0:
            return min(result, 2**31-1)
        else:
            return max(result, -2**31)
