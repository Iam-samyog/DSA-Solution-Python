class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarysearch(l,r,nums,target):
            while l<=r:
                mid=(l+r)//2
                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    return mid
            
            return -1
        
        left,right=0,len(nums)-1
        while left<right:
            m=(left+right)//2
            if nums[m]<nums[right]:
                right=m
            else:
                left=m+1
        

        pivot=left
        print(pivot)
        result=binarysearch(0,pivot-1,nums,target)
        print(result)
        if result!=-1:
            return result
        else:
            return binarysearch(pivot,len(nums)-1,nums,target)




                