class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]

        for i,v in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<v:
                ind=stack.pop()
                res[ind]=i-ind
            stack.append(i)
        
        return res

