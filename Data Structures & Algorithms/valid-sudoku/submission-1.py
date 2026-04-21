class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        #check the rows
        for row in range(9):
            seen=set()
            for i in range(9):
                if board[row][i]=='.':
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        #check the columns
        for cols in range(9):
            seen=set()
            for i in range(9):
                if board[i][cols]==".":
                    continue
                if board[i][cols] in seen:
                    return False
                seen.add(board[i][cols])
        
        #check sqaure
        for square in range(9):
            seen=set()
            for i in range(3):
                for j in range(3):
                    rows=(square//3)*3+i
                    cols=(square%3)*3+j
                    if board[rows][cols]=='.':
                        continue
                    if board[rows][cols] in seen:
                        return False
                    seen.add(board[rows][cols])
        return True

