class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r=0,len(nums)-1

        while l<r:
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        
        pivot=l

        def binarysearch(left,right):
            while left<=right:
                m=(left+right)//2

                if target>nums[m]:
                    left=m+1
                elif target<nums[m]:
                    right=m-1
                else:
                    return m
            return -1
        

        res=binarysearch(0,pivot-1)
        if res!=-1:
            return res
        
        return binarysearch(pivot,len(nums)-1)