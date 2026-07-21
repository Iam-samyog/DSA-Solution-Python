class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n1,n2=len(s1),len(s2)

        if n1>n2:
            return False
        
        sorted_s1=sorted(s1)

        for x in range(len(s2)):
            sub=sorted(s2[x:x+n1])
            if sub==sorted_s1:
                return True
        
        return False