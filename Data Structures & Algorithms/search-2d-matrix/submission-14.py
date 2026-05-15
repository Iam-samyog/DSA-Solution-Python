class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r,c=len(matrix),len(matrix[0])
        top,bot=0,r-1

        while top<=bot:
            row=(top+bot)//2

            if matrix[row][0]>target:
                bot=row-1
            elif matrix[row][-1]<target:
                top=row+1
            else:
                l,r=0,c-1
                while l<=r:
                    m=(l+r)//2
                    if target==matrix[row][m]:
                        return True
                    elif target>matrix[row][m]:
                        l=m+1
                    else:
                        r=m-1
                return False
            
        return False

        



        