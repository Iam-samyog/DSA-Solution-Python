class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r,c=len(matrix),len(matrix[0])
        top,bot=0,r-1

        while top<=bot:
            row=(top+bot)//2

            if matrix[row][-1]<target:
                top=row+1
            elif matrix[row][0]>target:
                bot=row-1
            else:
                left,right=0,c-1
                while left<=right:
                    m=(left+right)//2
                    if matrix[row][m]>target:
                        right=m-1
                    elif matrix[row][m]<target:
                        left=m+1
                    else:
                        return True
                return False
            
        return False 





        



        