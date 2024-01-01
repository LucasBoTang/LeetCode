class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # no intervals
        if not intervals:
            return []
        # sort by start time first
        intervals.sort()
        # init
        merged_intervals = [intervals[0]]
        # merge by iteration
        for start, end in intervals[1:]:
            # merge to previous
            if start <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(end, merged_intervals[-1][1])
            # new interval
            else:
                merged_intervals.append([start, end])
        return merged_intervals
