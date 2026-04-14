class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #optimal solution using Hashset
        longest=0
        
        for n in nums:
            current=n
            length=1

            while current+1 in nums:
                current+=1
                length+=1
            
            longest=max(length,longest)
        return longest
                