class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []

        if not candidates:
            return result

        candidates.sort()
        self.recursion(candidates, target, [], 0, result)

        return result


    def recursion(self, candidates, target, combination, start, result):
        """
        :type candidates: List[int]
        :type target: int
        :type combination: List[int]
        :type start: int
        :type result: List[List[int]]
        :rtype: void
        """

        if target == 0:
            if combination not in result:
                result.append(combination)
            return

        for i in range(start, len(candidates)):

            if candidates[i] > target:
                break

            self.recursion(candidates, target-candidates[i], combination+[candidates[i]], i+1, result)
