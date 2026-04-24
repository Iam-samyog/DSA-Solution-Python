class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res=set()
        nums.sort()

        for i in range(len(nums)):
            target=-nums[i]
            hashset=set()

            for j in range(i+1,len(nums)):
                remainder=target-nums[j]
                if remainder in hashset:
                    tri=tuple(sorted([nums[i],remainder,nums[j]]))
                    res.add(tri)
                hashset.add(nums[j])
            
        return [list(r) for r in res]

            