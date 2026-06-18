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
                mid=left+(right-left)//2
                if nums[mid]>target:
                    right=mid-1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    return mid
            return -1

        result=binarysearch(0,pivot-1)
        if result!=-1:
            return result
        
        return binarysearch(pivot,len(nums)-1)
                