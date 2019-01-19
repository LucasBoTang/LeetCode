class Solution(object):
    def poorPigs(self, buckets, die_minutes, test_minutes):
        """
        :type buckets: int
        :type die_minutes: int
        :type test_minutes: int
        :rtype: int
        """
        result = 0
        test_times = test_minutes // die_minutes
        while (test_times + 1) ** result < buckets:
            result += 1
        return result
