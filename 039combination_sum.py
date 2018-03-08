class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if not candidates:
            return result
        candidates = sorted(list(set(candidates)))
        self.recursion(candidates, target, [], 0, result)
        return result

    def recursion(self, candidates, target, combination, startindex, result):
        """
        :type candidates: List[int]
        :type target: int
        :type combination: List[int]
        :type startindex: int
        :type result: List[List[int]]
        :rtype: void
        """
        if target == 0:
            result.append(combination)
        for i in range(startindex, len(candidates)):
            if candidates[i] > target:
                break
            self.recursion(candidates, target-candidates[i], combination+[candidates[i]], i, result)
