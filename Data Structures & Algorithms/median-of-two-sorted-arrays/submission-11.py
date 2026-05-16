class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1,len2=len(nums1),len(nums2)

        i=j=0
        prev_median=median=0
        for count in range((len1+len2)//2 +1):
            prev_median=median

            if i<len1 and j<len2:
                if nums1[i]>nums2[j]:
                    median=nums2[j]
                    j+=1
                else:
                    median=nums1[i]
                    i+=1

            elif i<len1:
                median=nums1[i]
                i+=1
            else:
                median=nums2[j]
                j+=1
        
        if (len1+len2)%2==1:
            return float(median)
        else:
            return (prev_median+median)/2.0




        