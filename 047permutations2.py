class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        if not nums:
            return result

        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        self.recursion(num_count, [], result, len(nums))
        return result


    def recursion(self, num_count, permutation, result, length):
        """
        :type num_count: Dict[int]
        :type target: int
        :type permutation: List[int]
        :type result: List[List[int]]
        """

        if len(permutation) == length:
            result.append(permutation)
            return

        for num, count in num_count.items():
            if not count:
                continue
            num_count[num] -= 1
            self.recursion(num_count, permutation+[num], result, length)
            num_count[num] += 1
