class Solution:
    def trap(self, height: List[int]) -> int:
      

        if not height:
            return 0
        
        leftmax=[0]*len(height)
        rightmax=[0]*len(height)
        
        leftmax[0] = height[0]
        for i in range(1,len(height)):
            leftmax[i]=max(leftmax[i-1],height[i])
        
        rightmax[len(height)-1] = height[len(height)-1]

        for j in range(len(height)-2,-1,-1):
            rightmax[j]=max(rightmax[j+1],height[j])
        
        res = 0
        for i in range(len(height)):
            res += min(leftmax[i], rightmax[i]) - height[i]
        
        return res


        