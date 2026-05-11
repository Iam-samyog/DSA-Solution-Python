class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #Brute Force Approach

        for x in matrix:
            for y in x:
                if y==target:
                    return True
        return False
        