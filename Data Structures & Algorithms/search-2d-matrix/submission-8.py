class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

       #Optimal Code
        r,c=len(matrix),len(matrix[0])
        top,bot=0,r-1

        while top<=bot:
            row=(top+bot)//2
            if target>matrix[row][-1]:
                top=row+1
            elif target<matrix[row][0]:
                bot=row-1
            else:
                break
        

        if not top<=bot:
            return False
        
        row=(top+bot)//2
        i,j=0,c-1

        while i<=j:
            mid=(i+j)//2
            if target>matrix[row][mid]:
                i=mid+1
            elif target<matrix[row][mid]:
                j=mid-1
            else:
                return True
        return False
