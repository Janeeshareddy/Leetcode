class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]   
        valid=True
        for i in range(9):
            for j in range(9):
                value=board[i][j]
                if value==".":
                    continue
                box=(i//3)*3+(j//3)
                if (value in rows[i] or value in cols[j] or value in boxes[box]):
                    valid=False
                    break
                rows[i].add(value)
                cols[j].add(value)
                boxes[box].add(value)
        return valid