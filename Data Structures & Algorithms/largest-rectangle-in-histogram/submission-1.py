class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area=max(heights)

        for i in range(len(heights)):
            min_height=heights[i]
            for j in range(i+1,len(heights)):
                
                min_height=min(min_height,heights[j])
                width=j-i+1
                area=min_height*width
                max_area=max(max_area,area)
                

        return max_area
