from typing import List

class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: dp[i][0] = 1 for all i (one way to form the empty subsequence)
        for i in range(m + 1):
            dp[i][0] = 1
            
        # dp[0][j] remains 0 for j >= 1, because an empty s cannot form non-empty t.
        
        # Build the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    # If characters match, we have both choices.
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # Otherwise, skip s[i-1]
                    dp[i][j] = dp[i - 1][j]
        
        return dp[m][n]
