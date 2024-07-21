from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 行の探索
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        
        left, right = 0, COLS
        row = (top + bot) // 2
        while left <= right:
            col = (left + right) // 2
            if matrix[row][col] < target:
                left = col + 1
            elif matrix[row][col] > target:
                right = col - 1            
            else:
                return True

        return False

   
s = Solution()
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10

# matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
# target = 15

# matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
# target=11

print(s.searchMatrix(matrix=matrix, target=target))