class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mapping={'+': lambda a,b:a+b,'-': lambda a,b:a-b,'*': lambda a,b:a*b,'/':lambda a,b:a//b}
        stack=[]
        for c in tokens:
            if c in mapping:
                curr1=stack.pop()
                curr2=stack.pop()
                res=mapping[c](curr1,curr2)
                stack.append(res)
            else:
                stack.append(int(c))
        
        return stack.pop()

