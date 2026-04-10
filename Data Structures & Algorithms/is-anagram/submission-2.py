from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagram is the word formed by another word
        
        hashmap_1=dict()
        hashmap_2=dict()
        
        if(len(s)!=len(t)):
            return False
        
        for i in range(len(s)):
            if s[i] in hashmap_1:
                hashmap_1[s[i]]+=1
            else:
                hashmap_1[s[i]]=1
        
        for i in range(len(t)):
            if t[i] in hashmap_2:
                hashmap_2[t[i]]+=1
            else:
                hashmap_2[t[i]]=1

        return hashmap_1==hashmap_2

