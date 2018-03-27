# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key = lambda interval: interval.start)
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True
