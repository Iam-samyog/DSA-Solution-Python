class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=[]

        for strs in s:
            if strs.isalnum():
                cleaned.append(strs.lower())
        
        return cleaned==cleaned[::-1]
