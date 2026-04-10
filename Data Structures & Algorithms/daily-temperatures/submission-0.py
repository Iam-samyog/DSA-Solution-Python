class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[]
        n=len(temperatures)
     
        for i in range(n):
            count=0
            for j in range(i+1,n):
                if temperatures[j]>temperatures[i]:
                    count=j-i
                    break
            result.append(count)
            
                
        return result