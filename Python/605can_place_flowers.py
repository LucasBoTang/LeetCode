class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        cur_space = 0
        max_num = 0

        for i in [0] + flowerbed + [0]:
            if i:
                max_num += (cur_space - 1) // 2
                cur_space = 0
            else:
                cur_space += 1
        max_num += (cur_space - 1) // 2

        return n <= max_num
