class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashSet=set()

        for i in range(len(nums)):
            if nums[i] in hashSet:
                continue
            hashSet.add(nums[i])
        

        return len(hashSet)!=len(nums)