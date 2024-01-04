class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        # init slide window
        cur_satisfied = 0
        for i in range(len(customers)):
            # in the window
            if i < minutes:
                cur_satisfied += customers[i]
            # not grumpy
            elif not grumpy[i]:
                cur_satisfied += customers[i]
        # init max
        max_satisfied = cur_satisfied
        # slide window
        for i in range(minutes, len(customers)):
            start, end = i - minutes, i
            # left
            if grumpy[start]:
                cur_satisfied -= customers[start]
            # right
            if grumpy[end]:
                cur_satisfied += customers[end]
            # find max
            max_satisfied = max(max_satisfied, cur_satisfied)
        return max_satisfied
