from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # Create a 2D DP array of size (n + 1) x (amount + 1).
        # dp[i][j] will store the number of ways to make sum j using the first i coins.
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
        # Base Case: There is exactly 1 way to make sum 0 (by choosing no coins).
        for i in range(n + 1):
            dp[i][0] = 1
        
        # Build the DP table
        for i in range(1, n + 1):
            coin_value = coins[i - 1]
            for j in range(1, amount + 1):
                # 1) Exclude the current coin (use solutions from previous coins for sum j)
                dp[i][j] = dp[i - 1][j]
                
                # 2) Include the current coin if j >= coin_value.
                # Since it's the "unbounded" scenario, we do not move to i-1 but stay on i.
                if j >= coin_value:
                    dp[i][j] += dp[i][j - coin_value]
        
        # The answer is in dp[n][amount]: number of ways to form 'amount' with all n coins.
        return dp[n][amount]
