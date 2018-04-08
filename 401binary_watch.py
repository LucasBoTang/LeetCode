class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        for hour in range(12):
            for minute in range(60):
                if (bin(hour) + bin(minute)).count('1') == num:
                    result.append('{:d}:{:02d}'.format(hour, minute))
        return result
