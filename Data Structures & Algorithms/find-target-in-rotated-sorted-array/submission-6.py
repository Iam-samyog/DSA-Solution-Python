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
                if nums[m]<target:
                    left=m+1
                elif nums[m]>target:
                    right=m-1
                else:
                    return m
            return -1
        
        result=binarysearch(0,pivot-1)

        if result!=-1:
            return result
        
        return binarysearch(pivot,len(nums)-1)


            


        
        