class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        # addtional customers that can be satisfied
        additional_satisfied = [g * c for c, g in zip(customers, grumpy)]
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
            # left
            cur_satisfied -= additional_satisfied[i - minutes]
            # right
            cur_satisfied += additional_satisfied[i]
            # find max
            max_satisfied = max(max_satisfied, cur_satisfied)
        return max_satisfied
