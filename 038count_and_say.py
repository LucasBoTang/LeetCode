class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 1
        num = '1'
        while i != n:
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
            i +=1
        return num
