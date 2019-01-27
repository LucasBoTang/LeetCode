# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if not intervals:
            return []

        intervals.sort(key=lambda interval: interval.start)
        result = [intervals[0]]

        for interval in intervals[1:]:
            # merge
            if interval.start <= result[-1].end:
                result[-1].end = max(result[-1].end, interval.end)
            # not merge
            else:
                result.append(interval)

        return result
