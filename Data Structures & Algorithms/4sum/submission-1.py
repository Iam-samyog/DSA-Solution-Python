class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res=set()
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                val=target-nums[i]-nums[j]
                hash=set()
                for k in range(j+1,len(nums)):
                    remainder=val-nums[k]
                    if remainder in hash:
                        tmp=[nums[i],nums[j],nums[k],remainder]
                        res.add(tuple(sorted(tmp)))
                    hash.add(nums[k])
        
        return [list(i) for i in res]