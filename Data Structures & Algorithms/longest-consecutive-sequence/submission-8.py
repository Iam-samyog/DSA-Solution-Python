class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #optimal solution using Hashset
        longest=0
        HashSet=set(nums)
        
        for n in nums:
            if n-1 not in HashSet:
                length=1
                current=n
                while current+1 in HashSet:
                    current+=1
                    length+=1

                longest=max(length,longest)
                
        return longest
                