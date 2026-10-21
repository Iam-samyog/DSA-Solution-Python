class Solution:
    def isValid(self, s: str) -> bool:
        
        hash={
            ")":"(",
            "}":"{",
            "]":'['
        }

        stack=[]
        for x in s:
            if x in hash:
                if stack and hash[x]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        
        return True if not stack else False