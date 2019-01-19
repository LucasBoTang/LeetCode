class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(n + 1):
            if not i % 3:
                result.append('Fizz')
            elif not i % 5:
                result.append('Buzz')
            else:
                result.append(str(i))
        for i in range(n // 15 + 1):
            result[i * 15] = 'FizzBuzz'
        return result[1:]
