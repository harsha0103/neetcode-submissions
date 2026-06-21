class Solution:
    def countSubstrings(self, s: str) -> int:
        s1 = s
        s2 = s[::-1]
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        count = 0

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    

        for i in range(1,n+1):
            for j in range(1,n+1):
                if dp[i][j]!=0 and dp[i-1][j]!=dp[i][j]:
                    count+=1

        return count
