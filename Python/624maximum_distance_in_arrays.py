class Solution:
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """

        result = 0

        if len(arrays) < 2:
            return result

        cur_min, cur_max = arrays[0][0], arrays[0][-1]
        for i in range(1, len(arrays)):
            cur_row = arrays[i]
            result = max(result, abs(cur_max - cur_row[0]), abs(cur_row[-1] - cur_min))
            cur_min, cur_max = min(cur_min, cur_row[0]), max(cur_max, cur_row[-1])

        return result
