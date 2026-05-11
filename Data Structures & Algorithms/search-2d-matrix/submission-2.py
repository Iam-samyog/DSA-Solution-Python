class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #Second Approach (Try)

        for x in matrix:
            l,r=0,len(x)-1
            while l<=r:
                mid=l+(r-l)//2
                
                if x[mid]==target:
                    return True
                elif x[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
        
        return False
        