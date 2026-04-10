class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        operator=['+','-','*','/']
        answer=0
        

        for ch in tokens:
                       
            if ch in operator:
                b=stack.pop()
                a=stack.pop() 
                if ch=='+':
                    answer=a+b
                    stack.append(answer)
                elif ch=='*':
                    answer=a*b
                    stack.append(answer)
                elif ch=='/':
                    answer=int(a/b)
                   
                    stack.append(answer)
                elif ch=='-':
                    answer=a-b
                  
                    stack.append(answer)
                
            else:
                stack.append(int(ch))
        return stack[-1]
            
                    

        