from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        #Brute Force Approach

        s=sorted(s)
        t=sorted(t)

        return s==t
        