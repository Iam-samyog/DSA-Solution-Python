class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #binary search
        num=numbers
        for i in range(len(num)):
            l,r=i+1,len(num)-1
            temp=target-num[i]

            while l<=r:
                mid=l+(r-l)//2
                if num[mid]==temp:
                    return [i+1,mid+1]
                elif num[mid]>temp:
                    r=mid-1
                elif num[mid]<temp:
                    l=mid+1

        return []        
            
                