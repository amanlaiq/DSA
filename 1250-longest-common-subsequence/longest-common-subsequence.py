class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        # Create a 2D DP array with dimensions (n+1) x (m+1) initialized to 0.
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Build the DP table from row 1 to n and column 1 to m
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    # If characters match, add 1 to the result from the previous diagonal
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # Otherwise, take the maximum result from either ignoring the current char in text1 or text2
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        return dp[n][m]
