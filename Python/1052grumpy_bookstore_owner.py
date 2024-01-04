class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """

        # satisfication wihout technique
        original_satisfied = sum([(1 - g) * c for c, g in zip(customers, grumpy)])
        # addtional customers that can be satisfied
        additional_satisfied = [g * c for c, g in zip(customers, grumpy)]
        # init slide window
        cur_satisfied = original_satisfied + sum(additional_satisfied[:minutes])
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
