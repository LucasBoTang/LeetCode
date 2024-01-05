class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # init count
        island_cnt = 0
        # size of grid
        m, n = len(grid), len(grid[0])
        # init visited
        visited = set()
        # iterate all area
        for i in range(m):
            for j in range(n):
                # new land
                if grid[i][j] == "1" and (i, j) not in visited:
                    # visit whole island
                    self.bfs(grid, i, j, visited)
                    # get a new island
                    island_cnt += 1
        return island_cnt

    def bfs(self, grid, i, j, visited):
        # size of grid
        m, n = len(grid), len(grid[0])
        # init queue
        queue = collections.deque()
        queue.append((i, j))
        # adjancancy
        adjancancy = [(-1,0), (1,0), (0,-1), (0,1)]
        # start bfs
        while queue:
            # dequeue
            x, y = queue.popleft()
            # neighbors
            for dx, dy in adjancancy:
                new_x, new_y = x + dx, y + dy
                # avoid the out of bound
                if new_x < 0 or new_x > m - 1 or new_y < 0 or new_y > n - 1:
                    continue
                # is land and unvisited
                if grid[new_x][new_y] == "1" and (new_x, new_y) not in visited:
                    # enqueue
                    queue.append(((new_x, new_y)))
                    visited.add((new_x, new_y))


