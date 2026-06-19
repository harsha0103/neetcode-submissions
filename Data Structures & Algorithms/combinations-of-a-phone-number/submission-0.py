class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        res=[]

        if digits=='':
            return []

        
        def dfs(curr_str,i):
            if len(curr_str)==len(digits):
                res.append(curr_str)
                return 
            for c in mapping[digits[i]]:
                dfs(curr_str+c,i+1)

        
        dfs('',0)
        return res

