class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # remainder=0
        # hashMap=dict()

        # for i in range(len(nums)):
        #     remainder=target-nums[i]
        #     if remainder in hashMap:
        #         return [hashMap[remainder],i]
        #     hashMap[nums[i]]=i
        

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]