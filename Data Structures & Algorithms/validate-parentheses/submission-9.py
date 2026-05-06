class Solution:
    def isValid(self, s: str) -> bool:
        hash={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack=[]

        for c in s:
            if c in hash:
                if stack and hash[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:

                stack.append(c)

        return True if not stack else False        