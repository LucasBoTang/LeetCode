class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        result = 0
        hash_table = set()
        m, n = len(grid), len(grid[0])

        for r in range(m):
            for c in range(n):
                pos = (r, c)

                if grid[r][c] and pos not in hash_table:
                    queue = [pos]
                    hash_table.add(pos)
                    cur_area = 1

                    while queue:
                        new_queue = []

                        for loc in queue:
                            i, j = loc
                            poses = []

                            if i != 0 and grid[i-1][j]:
                                poses.append((i-1, j))
                            if i != m-1 and grid[i+1][j]:
                                poses.append((i+1, j))
                            if j != 0 and grid[i][j-1]:
                                poses.append((i, j-1))
                            if j != n-1 and grid[i][j+1]:
                                poses.append((i, j+1))

                            for pos in poses:
                                if pos not in hash_table:
                                    cur_area += 1
                                    new_queue.append(pos)
                                    hash_table.add(pos)

                        queue = new_queue

                    result = max(result, cur_area)

        return result
