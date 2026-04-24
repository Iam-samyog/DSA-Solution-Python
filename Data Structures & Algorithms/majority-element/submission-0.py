class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count={}

        for c in nums:
            count[c]=1+count.get(c,0)
        
        for n,c in count.items():
            if c>(len(nums)/2):
                return n
        

        