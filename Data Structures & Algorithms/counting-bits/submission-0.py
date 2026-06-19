class Solution:
    def countBits(self, n: int) -> List[int]:
        output=[]
        def dfs(n1):
            count=0

            while n1>0:
                if n1 & 1:
                    count+=1
                n1=n1>>1 
            return count
        
        for i in range(n+1):
            output.append(dfs(i))
        
        return output 