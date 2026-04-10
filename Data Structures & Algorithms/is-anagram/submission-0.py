from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagram is the word formed by another word
        
        return Counter(s)==Counter(t)
       
                
        
