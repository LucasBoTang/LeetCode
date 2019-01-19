class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(points)):
            dist2_hash = {}
            for j in range(len(points)):
                if i == j:
                    continue
                dist2 = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                dist2_hash[dist2] = dist2_hash.get(dist2, 0) + 1
            for v in dist2_hash.values():
                if v > 1:
                    result += v * (v - 1)
        return result
