class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        start, end = 0, len(height) - 1

        water = 0
        while start < end:
            width = end - start

            if height[start] > height[end]:
                water = max(water, width*height[end])
                end -= 1
            else:
                water = max(water, width*height[start])
                start += 1

        return water
