class Solution:
    def trap(self, height: List[int]) -> int:
      

        # if not height:
        #     return 0
        
        # l,r=0,len(height)-1

        # leftmax=height[l]
        # rightmax=height[r]

        # res=0
        # while l<r:
        #     if leftmax<rightmax:
        #         l+=1
        #         leftmax=max(leftmax,height[l])
        #         res+=leftmax-height[l]
        #     else:
        #         r-=1
        #         rightmax=max(rightmax,height[r])
        #         res+=rightmax-height[r]

        # return res

        if not height:
            return 0
        res=0
        for i in range(len(height)):
            leftmax=rightmax=height[i]

            for j in range(i):
                leftmax=max(leftmax,height[j])

            for j in range(i+1,len(height)):
                rightmax=max(rightmax,height[j])
            
            res+=min(leftmax,rightmax)-height[i]
        
        return res
        