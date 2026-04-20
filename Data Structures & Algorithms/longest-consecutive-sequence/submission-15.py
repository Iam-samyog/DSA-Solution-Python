class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hashset=set(nums)
        longest=0
        for s in nums:
            if s-1 not in hashset:
                current=s
                length=1
                while current+1 in hashset:
                    current+=1
                    length+=1
                longest=max(length,longest)
        
        return longest