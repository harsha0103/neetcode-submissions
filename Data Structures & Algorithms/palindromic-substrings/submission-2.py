class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        res = 0

        for i in range(1, n + 1):  # i = end index (1-based)
            for j in range(1, i + 1):  # j = start index (1-based)
                if s[i - 1] == s[j - 1]:
                    if i - j <= 1 or dp[i - 1][j + 1]:  # check inner substring
                        dp[i][j] = True
                        res += 1

        return res
