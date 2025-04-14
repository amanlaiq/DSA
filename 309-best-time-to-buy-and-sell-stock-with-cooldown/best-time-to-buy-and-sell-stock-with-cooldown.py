from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        
        # Initialize the DP arrays for each state.
        s0 = [0] * n   # Rest state: not holding stock, free to buy.
        s1 = [0] * n   # Hold state: currently holding stock.
        s2 = [0] * n   # Cooldown state: just sold stock, cannot buy today.
        
        # Base conditions for day 0:
        s0[0] = 0               # If you do nothing on day 0, profit is 0.
        s1[0] = -prices[0]      # If you buy on day 0, profit is -prices[0].
        s2[0] = float('-inf')   # Cooldown is not possible on day 0.
        
        # Build the DP states day by day.
        for i in range(1, n):
            # Rest state: either we continue resting or just came from a cooldown.
            s0[i] = max(s0[i-1], s2[i-1])
            # Hold state: either we continue holding or we buy today (from rest state).
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])
            # Cooldown state: we can only reach here by selling today.
            s2[i] = s1[i-1] + prices[i]
        
        # The final profit must be in a state where we are not holding a stock.
        return max(s0[n-1], s2[n-1])
