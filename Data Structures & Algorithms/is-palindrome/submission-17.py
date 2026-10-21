class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        str_en=""
        for x in s:
            if x.isalnum():
                str_en+=x.lower()
        
        reverse=str_en[::-1]
        return reverse==str_en
