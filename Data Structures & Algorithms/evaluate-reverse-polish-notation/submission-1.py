class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=''
        app=''
        while len(tokens)>0:
            num1=tokens.pop()
            
            if not(num1.isdigit()):
                num2=tokens.pop()
                res=res+')'+num2+num1
                app=app+'('
                
            else:
                res=res+num1
        return eval(app+res[::-1])



        