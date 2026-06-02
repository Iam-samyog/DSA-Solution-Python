class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n=len(heights)
        max_area=0
        stack=[] #height,index

        for i,height in enumerate(heights):
            start=i
            while stack and stack[-1][0]>height:
                h,j= stack.pop()
                w=i-j
                a=w*h
                max_area=max(a,max_area)
                start=j
        
            stack.append((height,start))
        

        while stack:
            h,j=stack.pop()
            w=n-j
            max_area=max(max_area,w*h)

        return max_area

            


            
