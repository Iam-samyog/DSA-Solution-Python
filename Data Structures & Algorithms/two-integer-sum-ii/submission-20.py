class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Optimal Solution
        #using two pointer

        #binary search

        for i in range(len(numbers)):
            l=i+1
            r=len(numbers)-1
            tmp = target - numbers[i]

            while l<=r:
                mid=(l+r)//2
                if numbers[mid]==tmp:
                    return [i+1,mid+1]
                elif numbers[mid]>tmp:
                    r=mid-1
                else:
                    l=mid+1
