class Solution:
    def findMin(self, nums: List[int]) -> int:

        rem=nums[0]
        for n in nums:
            if rem>n:
                rem=n
        return rem

