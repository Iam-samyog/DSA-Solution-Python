class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #HashMap
        count1={}

        for c in s1:
            count1[c]=1+count1.get(c,0)
        
        need=len(count1)

        for i in range(len(s2)):
            count=0
            count2={}
            for j in range(i,len(s2)):
                count2[s2[j]]=1+count2.get(s2[j],0)

                if count1.get(s2[j],0)<count2.get(s2[j],0):
                    break
                
                if count1.get(s2[j],0)==count2.get(s2[j],0):
                    count+=1
                
                if count==need:
                    return True
        
        return False 




            
        