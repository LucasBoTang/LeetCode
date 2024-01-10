class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # init dp memo for the first house
        r, g, b = costs[0]
        # iterate by painting the next house
        for cost_r, cost_g, cost_b in costs[1:]:
            # update previous costs
            prev_r, prev_g, prev_b = r, g, b
            # paint red
            r = cost_r + min(prev_g, prev_b)
            # paint green
            g = cost_g + min(prev_r, prev_b)
            # paint blue
            b = cost_b + min(prev_r, prev_g)
        # get the minimum cost
        return min(r, g, b)
