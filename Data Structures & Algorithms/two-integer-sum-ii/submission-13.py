class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # l,r=0,len(numbers)-1

        # while l<r:
        #     currSum=numbers[l]+numbers[r]

        #     if currSum>target:
        #         r-=1
        #     elif currSum <target:
        #         l+=1
        #     else:
        #         return [l+1,r+1]

        # return []

        hashmap={}
        nums=numbers
        for i in range(len(nums)):
            remainder=target-nums[i]
            if remainder in hashmap:
                return [hashmap[remainder]+1,i+1]
            hashmap[nums[i]]=i
        

            
