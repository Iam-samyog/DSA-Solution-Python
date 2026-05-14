class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Binary Search

        r,c=len(matrix),len(matrix[0])

        top,bot=0,r-1

        while top<=bot:
            row=(top+bot)//2
            if target>matrix[row][-1]:
                top=row+1
            elif target<matrix[row][0]:
                bot=row-1
            else:
                left,right=0,c-1
                while left<=right:
                    m=(left+right)//2
                    if target==matrix[row][m]:
                        return True
                    elif target>matrix[row][m]:
                        left=m+1
                    else:
                        right=m-1
                return False
        
        return False



        