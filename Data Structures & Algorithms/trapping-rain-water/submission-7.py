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

        # if not height:
        #     return 0
        # res=0
        # for i in range(len(height)):
        #     leftmax=rightmax=height[i]

        #     for j in range(i):
        #         leftmax=max(leftmax,height[j])

        #     for j in range(i+1,len(height)):
        #         rightmax=max(rightmax,height[j])
            
        #     res+=min(leftmax,rightmax)-height[i]
        
        # return res

        if not height:
            return 0
        n=len(height)
        leftmax=[0]*n
        rightmax=[0]*n

        leftmax[0]=height[0]
        for i in range(1,len(leftmax)):
            leftmax[i]=max(leftmax[i-1],height[i])
        rightmax[n-1]=height[n-1]

        for i in range(len(rightmax)-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],height[i])

        minimum=0
        res=0
        for i in range(len(leftmax)):
            minimum=min(leftmax[i],rightmax[i])
            res+=minimum-height[i]
        
        return res


        