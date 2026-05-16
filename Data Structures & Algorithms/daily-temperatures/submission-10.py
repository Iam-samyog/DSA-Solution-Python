class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack=[]
        for i in range(len(temperatures)):
            temp=0
            for j in range(i+1,len(temperatures)):
                if temperatures[i]<temperatures[j]:
                    temp=j-i
                    break
            
            stack.append(temp)
        
        return stack


        


            

                    