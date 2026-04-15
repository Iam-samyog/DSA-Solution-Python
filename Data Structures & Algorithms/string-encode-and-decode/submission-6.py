class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""

        for e in strs:
            encoded+=str(len(e))+"#"+e
        
        return encoded
        

    def decode(self, s: str) -> List[str]:

        
        i=0
        res=[]

        while i<len(s):
            j=i

            #to find the length
            while s[j]!="#":
                j+=1
            
            length=int(s[i:j])

            #print
            word=s[j+1:j+1+length]
            res.append(word)

            i=j+1+length

        return res

