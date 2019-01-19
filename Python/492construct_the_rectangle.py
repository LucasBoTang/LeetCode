class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        W = int(area ** 0.5)
        while area % W:
            W -= 1
        return [area // W, W]
