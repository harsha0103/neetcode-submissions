class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mapping ={
            '+': lambda a,b:a+b,
            '-': lambda a,b:a-b,
            '*': lambda a,b:a*b,
            '/': lambda a,b:int(float(b)/a)
        }
        stack=[]
        for i in tokens:
            if i in mapping:
               b=stack.pop() 
               a=stack.pop()
               res=mapping[i](a,b)
               stack.append(res)
            else:
                stack.append(int(i))
        
        final=stack.pop()
        return final