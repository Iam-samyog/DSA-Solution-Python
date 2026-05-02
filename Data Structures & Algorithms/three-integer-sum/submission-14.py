class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            target=-nums[i]
            l,r=i+1,len(nums)-1

            #Two sum II
            while l<r:
                currSum=nums[l]+nums[r]
                if currSum>target:
                    r-=1
                elif currSum<target:
                    l+=1
                else:
                    res.append([nums[l],nums[r],nums[i]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        
        return res

