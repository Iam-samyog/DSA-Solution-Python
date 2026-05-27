class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""

        countT={}

        for x in t:
            countT[x]=1+countT.get(x,0)
        
        res=[1,1]
        minlen=float('inf')

        for i in range(len(s)):
            countS={}
            for j in range(i,len(s)):
                countS[s[j]]=1+countS.get(s[j],0)

                match=True

                for c in countT:
                    if countS.get(c,0)<countT[c]:
                        match=False
                        break
                
                if match and (j-i+1)<minlen:
                    minlen=j-i+1
                    res=[i,j]
        
        l,r=res
        return s[l:r+1] if minlen!=float('inf') else ""
        