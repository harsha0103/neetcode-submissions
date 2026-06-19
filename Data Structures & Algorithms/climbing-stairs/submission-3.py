class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n<=2:
            return n
        
        memo={}
        if n in memo:
            return memo[n]

        memo[n]= self.climbStairs(n-1)+self.climbStairs(n-2)
        return memo[n]