class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res=set()
        nums.sort()
        n=len(nums)
        for i in range(n):
            

            target=-nums[i]
            hashmap={}
            for j in range(i+1,n):
                rem=target-nums[j]
                if rem in hashmap:
                    res.add(tuple([nums[i],nums[j],rem]))
                
                hashmap[nums[j]]=j

        return [list(r) for r in res]             

