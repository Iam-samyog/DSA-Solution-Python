class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0

        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                h=min(heights[i],heights[j])
                w=j-i
                area=h*w
                res=max(area,res)
        return res


