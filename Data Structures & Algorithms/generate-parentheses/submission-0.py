class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        substr=[]
        
        def backtrack(op,cl):
            if op==cl==n:
                res.append(''.join(substr))
                return 
            
            if op<n:
                substr.append('(')
                backtrack(op+1,cl)
                substr.pop()
            if cl<op:
                substr.append(')')
                backtrack(op,cl+1)
                substr.pop()
        
        backtrack(0,0)
        return res

        