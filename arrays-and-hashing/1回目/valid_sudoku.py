from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])
                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])   

                if board[i][j] in squares[(i//3, j//3)]:
                    return False
                squares[(i//3, j//3)].add(board[i][j])
        
        return True
    
s = Solution()
board=[["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","1",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]
print(s.isValidSudoku(board))


