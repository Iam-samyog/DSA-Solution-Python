from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # #0(1)-Space Complexity 
        # if len(s)!=len(t):
        #     return False
        
        # countS,countT={},{}

        # for i in range(len(s)):
        #     countS[s[i]]=1+countS.get(s[i],0)
        #     countT[t[i]]=1+countT.get(t[i],0)

        # for c in countT:
        #     if countT[c]!=countS.get(c,0):
        #         return False
            
        # return True 

        if len(s)!=len(t):
            return False
        
        s_length=[0]*26
       

        for i in s:
            s_length[ord(i)-ord('a')]+=1
        for j in t:
            s_length[ord(j)-ord('a')]-=1
        
        for val in s_length:
            if val!=0:
                return False
        
        return True