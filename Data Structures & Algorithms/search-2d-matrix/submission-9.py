class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                # Target must be in this row or nowhere
                l, r = 0, COLS - 1
                while l <= r:
                    m = (l + r) // 2
                    if target > matrix[row][m]:
                        l = m + 1 # Fixed: Search right
                    elif target < matrix[row][m]:
                        r = m - 1 # Fixed: Search left
                    else:
                        return True
                
                # If inner search finishes without finding target, 
                # it's not in the matrix.
                return False 
                
        return False