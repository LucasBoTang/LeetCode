class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 9

        num = 10 ** n - 1
        lower, upper = 10 ** (n - 1), 10 ** n - 1

        while True:
            palindrome = int(str(num) + str(num)[::-1])
            if upper * upper < palindrome:
                num -= 1
                continue
            sqrt = int(palindrome ** 0.5)
            product = upper

            while product > sqrt:
                if palindrome % product == 0:
                    return palindrome % 1337
                product -= 1

            num -= 1
