from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        # If total is less than |target| or (total + target) is odd, no solution exists.
        if total < abs(target) or (total + target) % 2 != 0:
            return 0
        
        S = (total + target) // 2
        n = len(nums)
        
        # dp[i][j]: number of ways to form sum j using the first i elements.
        # We need dimensions (n+1) x (S+1).
        dp = [[0] * (S + 1) for _ in range(n + 1)]
        
        # Base Case: There's exactly 1 way to form sum 0 (by choosing nothing) for any prefix.
        for i in range(n + 1):
            dp[i][0] = 1
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(0, S + 1):
                # Do not choose the i-th element (nums[i-1])
                dp[i][j] = dp[i - 1][j]
                # If the current element can be used, add the ways to form the remaining sum.
                if nums[i - 1] <= j:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]
        
        return dp[n][S]
