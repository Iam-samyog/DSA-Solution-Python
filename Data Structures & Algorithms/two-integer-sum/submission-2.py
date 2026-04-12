class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # remainder=0
        # hashMap=dict()

        # for i in range(len(nums)):
        #     remainder=target-nums[i]
        #     if remainder in hashMap:
        #         return [hashMap[remainder],i]
        #     hashMap[nums[i]]=i

        sorted(nums)
        for i in range(len(nums)):
            remainder=target-nums[i]
            for j in range(i+1,len(nums)):
                if remainder==nums[j]:
                    return [i,j]

        