class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        while len(numbers) < 2:
            return result
        start, end = 0, len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] < target:
                start += 1
            if numbers[start] + numbers[end] > target:
                end -= 1
            if numbers[start] + numbers[end] == target:
                result = [start + 1, end + 1]
                return result
        return result
