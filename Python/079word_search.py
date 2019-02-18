class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        m, n = len(board), len(board[0])
        visited = [[False] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and board[i][j] == word[0]:
                    if self.dfs(board, word[1:], i, j, m, n, visited):
                        return True
                    # track back visited
                    visited[i][j] = False

        return False

    def dfs(self, board, word, i, j, m, n, visited):
        """
        """

        visited[i][j] = True

        if len(word) == 0:
            return True

        # left, right, dwon, up
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

        for r, c in neighbors:
            # out of bounds
            if r < 0 or r >= m or c < 0 or c >= n:
                continue
            # visited or not matching
            if visited[r][c] or board[r][c] != word[0]:
                continue
            if self.dfs(board, word[1:], r, c, m, n, visited):
                return True
            # track back visited
            visited[r][c] = False

        return False
