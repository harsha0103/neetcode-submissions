class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mapping ={
            '+': lambda a,b:a+b,
            '-': lambda a,b:a-b,
            '*': lambda a,b:a*b,
            '/': lambda a,b:a/b
        }
        stack=[]
        for i in tokens:
            if i in mapping:
               a=stack.pop() 
               b=stack.pop()
               res=mapping[i](a,b)
               stack.append(res)
            else:
                stack.append(int(i))
        
        final=int(stack.pop())
        return final