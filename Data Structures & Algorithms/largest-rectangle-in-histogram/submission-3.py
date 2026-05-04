class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area=max(heights)
        for i in range(len(heights)):
            min_height=heights[i]

            for j in range(i+1,len(heights)):
                min_height=min(min_height,heights[j])
                w=j-i+1
                max_area=max(w*min_height,max_area)
            
        return max_area
                
            
