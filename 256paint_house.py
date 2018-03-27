class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        cur = [0] * 3
        for next in costs:
            cur = [next[i] + min(cur[:i] + cur[i+1:]) for i in range(3)]
        return min(cur)
