class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0

        if k == 0:
            counts = {}
            for num in nums:
                counts[num] = counts.get(num, 0) + 1
            for count in counts.values():
                if count > 1:
                    result += 1


        elif k > 0:
            hash_map = {} # use dictionary for O(1) search
            for num in nums:
                if num not in hash_map:
                    hash_map[num] = 1
                    if num - k in hash_map:
                        result += 1
                    if num + k in hash_map:
                        result += 1

        return result
