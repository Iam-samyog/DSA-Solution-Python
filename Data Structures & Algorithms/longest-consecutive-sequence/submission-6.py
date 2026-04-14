class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #optimal solution using Hashset

        longest=0
        nums_set=set(nums)

        for i in range(len(nums)):
            if nums[i]-1 not in nums_set:
                length=1
                current=nums[i]

                while current+1 in nums_set:
                    current+=1
                    length+=1

                longest=max(length,longest)
        
        return longest

                