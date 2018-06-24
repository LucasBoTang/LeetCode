class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        hash_set = set(candies)
        return min(len(hash_set), len(candies) // 2)
