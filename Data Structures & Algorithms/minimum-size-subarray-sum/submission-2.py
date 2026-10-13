class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best=float("inf")
        sums=0
        l=0
        for r in range(len(nums)):
            sums+=nums[r]
            while sums>=target:
                best=min(best,r-l+1)
                sums-=nums[l]
                l+=1
        
        return 0 if best==float("inf") else best