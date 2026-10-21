class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res=set()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            hashmap={}
            for j in range(i+1,len(nums)):
                rem=target-nums[j]
                if rem in hashmap:
                    res.add(tuple([nums[i],nums[j],rem]))
                hashmap[nums[j]]=j
            
        
        return list(res)
            