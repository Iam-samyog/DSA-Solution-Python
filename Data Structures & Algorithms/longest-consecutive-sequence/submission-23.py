class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashset=set(nums)
        res=0
        for x in nums:
            if x-1 not in hashset:
                curr=x
                curr_s=1
                while curr+1 in hashset:
                    curr_s+=1
                    curr+=1
                res=max(res,curr_s)

        
        return res