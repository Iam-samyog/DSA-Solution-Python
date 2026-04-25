class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        nums=numbers
        l,r=0,len(nums)-1

        while l<r:
            currSum=nums[l]+nums[r]
            if currSum>target:
                r-=1
            elif currSum<target:
                l+=1
            else:
                return [l+1,r+1]
         
        

            
