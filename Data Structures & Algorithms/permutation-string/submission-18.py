class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count1=Counter(s1)

        need=len(count1)
        
        for j in range(len(s2)):
            count2={}
            curr=0
            for i in range(j,len(s2)):
                count2[s2[i]]=1+count2.get(s2[i],0)

                if count2[s2[i]]>count1.get(s2[i],0):
                    break
                
                if count2[s2[i]]==count1.get(s2[i],0):
                    curr+=1
                
                if curr==need:
                    return True
        
        return False