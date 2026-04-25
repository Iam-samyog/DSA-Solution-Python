class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        nums=numbers
        seen={}
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in seen:
                return [seen[rem]+1,i+1]
            seen[nums[i]]=i        
        

            
