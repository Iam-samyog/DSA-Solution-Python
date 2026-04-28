class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res=0
        hashset=set(nums)

        for n in nums:
            streak=0
            curr=n

            while curr in hashset:
                curr+=1
                streak+=1
            res=max(res,streak)
        return res