class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Optimal Solution
        #using two pointer

        l=0
        r=len(numbers)-1

        while l<r:
            currSum=numbers[l]+numbers[r]
            if currSum>target:
                r-=1
            elif currSum<target:
                l+=1
            elif currSum==target:
                return [l+1,r+1]
        
        return []

            
           
            
                