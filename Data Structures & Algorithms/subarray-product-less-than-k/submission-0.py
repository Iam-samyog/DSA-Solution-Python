class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        l=0
        curr_product=1
        res=[]
        for r in range(len(nums)):
            curr_product*=nums[r]
            while curr_product>=k and l<=r:
                curr_product//=nums[l]
                l+=1
            
            res.append(r-l+1)
        
        return sum(res)
