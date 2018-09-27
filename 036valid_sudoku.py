class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):
            rows = set()
            cols = set()
            subs = set()

            for j in range(9):
                row_num = board[i][j]
                col_num = board[j][i]
                sub_num = board[i//3*3+j//3][i%3*3+j%3]

                if row_num == '.':
                    pass
                elif row_num not in rows:
                    rows.add(row_num)
                else:
                    return False

                if col_num == '.':
                    pass
                elif col_num not in cols:
                    cols.add(col_num)
                else:
                    return False

                if sub_num == '.':
                    pass
                elif sub_num not in subs:
                    subs.add(sub_num)
                else:
                    return False

        return True
