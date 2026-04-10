class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hash={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        

        for ch in s:
            if ch in hash.values():
                stack.append(ch)
            else:
                if not stack or stack[-1]!=hash[ch]:
                    return False
                stack.pop()
        
        return not stack