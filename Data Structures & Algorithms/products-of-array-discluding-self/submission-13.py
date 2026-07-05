class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        pre=1
        post=1

        for i in range(len(nums)):
            ans[i]=pre
            pre*=nums[i]
        
        for j in range(len(nums)-1,-1,-1):
            ans[j]*=post
            post*=nums[j]
        
        return ans
                
                