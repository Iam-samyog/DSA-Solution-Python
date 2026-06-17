class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num=Counter(nums)
        stack=[]
        for k,v in num.items():
            if v> (len(nums)//3):
                stack.append(k)
        return stack