class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for x in range(k+1,len(nums)):
                        sum_=nums[i]+nums[j]+nums[k]+nums[x]
                        if sum_==target:
                            res.add(tuple(sorted([nums[i],nums[j],nums[k],nums[x]])))
        
        return [list(i) for i in res]