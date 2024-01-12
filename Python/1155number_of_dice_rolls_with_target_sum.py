class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        # divider
        mod = 10 ** 9 + 7
        # special cases
        if n == 0 or n * k < target or n > target:
            return 0
        # init table
        dp_table = [[0] * (target + 1) for _ in range(n + 1)]
        dp_table[0][0] = 1
        # throw one die for each iteration
        for i in range(1, n + 1):
            # for each possible sum
            for j in range(1, target + 1):
                # the face of die
                for l in range(1, k + 1):
                    # out of bound
                    if l > j:
                        continue
                    # add ways
                    dp_table[i][j] +=  dp_table[i - 1][j - l]
                # modulo
                dp_table[i][j] %= mod
        return dp_table[n][target] 
        
