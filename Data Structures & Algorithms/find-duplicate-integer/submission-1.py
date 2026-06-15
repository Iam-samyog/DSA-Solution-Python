class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Negative Marking

        for n in nums:
            index=abs(n)-1
            if nums[index]>0:
                nums[index]=-nums[index]
            else:
                return abs(n)
        
        
