class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = '1'
        for _ in range(n-1):
            temp = num[0]
            count = 0
            cur = ''
            for j in range(len(num)):
                if temp == num[j]:
                    count += 1
                else:
                    cur += str(count) + temp
                    temp = num[j]
                    count = 1
            num = cur + str(count) + temp
        return num
