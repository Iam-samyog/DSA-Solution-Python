class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # remainder=0
        # hashMap=dict()

        # for i in range(len(nums)):
        #     remainder=target-nums[i]
        #     if remainder in hashMap:
        #         return [hashMap[remainder],i]
        #     hashMap[nums[i]]=i

        rem=0
        HashMap=dict()

        for i in range(len(nums)):
            remainder=target-nums[i]
            if remainder in HashMap:
                return [HashMap[remainder],i]
            HashMap[nums[i]]=i

        