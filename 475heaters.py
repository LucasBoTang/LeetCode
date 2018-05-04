class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        result = heaters[0] - houses[0]
        i, j = 1, 1
        while i < len(houses) and j < len(heaters):
            if houses[i] >= heaters[j]:
                j += 1
            else:
                cur = min(heaters[j] - houses[i], houses[i] - heaters[j-1])
                result = max(result, cur)
                i += 1
        result = max(result, houses[-1] - heaters[-1])
        return result
