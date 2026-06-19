class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator={
            '+':lambda a,b: int(a+b),
            '-':lambda a,b: int(a-b),
            '*':lambda a,b: int(a*b),
            '/':lambda a,b: int(a/b),
        }
        stack=[]
        for char in tokens:
            if char in operator:
                num1=stack.pop()
                num2=stack.pop()
                res=operator[char](num2,num1)
                stack.append(res)
            else:
                stack.append(int(char))
        return stack[0]



        