class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        hash={
            ')':'(',
            '}':'{',
            ']':'['
        }

        for a in s:
            if a in hash:
                if stack and stack[-1]==hash[a]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(a)

        return True if not stack else False

            
                

    
        