class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        result = 0
        INT_MIN, INT_MAX = - 2 ** 31, 2 ** 31 - 1

        index = 0
        sign = 1
        while index < len(str):
            if str[index].isspace():
                index += 1
            elif str[index] == '-':
                sign = - 1
                index += 1
                break
            elif str[index] == '+':
                index += 1
                break
            else:
                break

        while index < len(str) and str[index].isdigit():
            result = result * 10 + int(str[index])
            index += 1
        result *= sign

        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result
