class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        remainder=0
        hashMap={}

        for i in range(len(nums)):
            remainder=target-nums[i]
            if remainder in hashMap:
                return [hashMap[remainder],i]
            hashMap[nums[i]]=i     