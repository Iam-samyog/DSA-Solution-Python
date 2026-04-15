from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagram is the word formed by another word
        # if len(s)!=len(t):
        #     return False
        
        # countS,countT={},{}

        # for i in range(len(s)):
        #     countS[s[i]]=1+countS.get(s[i],0)
        #     countT[t[i]]=1+countT.get(t[i],0)
        # for c in countS:
        #     if countS[c]!=countT.get(c,0):
        #         return False
        # return True
        

        s_array=[0]*26
        t_array=[0]*26
        for i in s:
            s_array[ord(i)-ord('a')]+=1
        for i in t:
            t_array[ord(i)-ord('a')]+=1
        
        return s_array==t_array