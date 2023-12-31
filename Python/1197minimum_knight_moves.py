class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # all move dirctions
        move = [(1,2), (2,1), (1,-2), (2,-1), 
                (-1,2), (-2,1), (-1,-2), (-2,-1)]
        # start from orignal point
        queue = collections.deque([(0, 0)])
        dist = {(0, 0): 0}
        # bfs
        while queue:
            cur_x, cur_y = queue.popleft()
            # achive destination
            if (cur_x, cur_y) == (x, y):
                return dist[cur_x, cur_y]
            # move to neighbors
            for dx, dy in move:
                new_x, new_y = cur_x + dx, cur_y + dy
                # not visited
                if (new_x, new_y) not in dist:
                    dist[new_x, new_y] = dist[cur_x, cur_y] + 1
                    queue.append((new_x, new_y))
        return -1
