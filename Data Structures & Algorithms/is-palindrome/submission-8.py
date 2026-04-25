class Solution:
    def isPalindrome(self, s: str) -> bool:
        #
        l,r=0,len(s)-1
        string=s.lower()

        while l<r:
            while not string[l].isalnum() and l<r:
                l+=1
            while not string[r].isalnum() and r>l:
                r-=1
            
            if string[l]!=string[r]:
                return False
            
            l+=1
            r-=1
        return True