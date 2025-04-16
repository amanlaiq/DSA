from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # dp[i][j] will represent the maximum cherries we can collect when:
        #   - Person 1 is at (i, k-i)
        #   - Person 2 is at (j, k-j)
        # after taking k steps.
        dp = [[-float('inf')] * n for _ in range(n)]
        dp[0][0] = grid[0][0]  # Both start at (0,0)
        
        # Total number of steps taken by each person
        # Maximum steps = (n-1)+(n-1) = 2*n-2
        for k in range(1, 2 * n - 1):
            # Initialize a new dp table for the current step.
            new_dp = [[-float('inf')] * n for _ in range(n)]
            # i and j represent the row indices for person 1 and person 2 respectively.
            # Given k, the corresponding column for person 1 is k-i, and for person 2 is k-j.
            for i in range(max(0, k - (n - 1)), min(n, k + 1)):
                for j in range(max(0, k - (n - 1)), min(n, k + 1)):
                    # The columns based on the steps:
                    c1, c2 = k - i, k - j
                    # They must be within bounds.
                    if c1 >= n or c2 >= n or grid[i][c1] == -1 or grid[j][c2] == -1:
                        continue
                    # If the two persons are at the same cell, count cherries only once.
                    value = grid[i][c1] if i == j and c1 == c2 else grid[i][c1] + grid[j][c2]
                    
                    # Try all four ways they could have moved from the previous step (k-1):
                    for di in [0, 1]:
                        for dj in [0, 1]:
                            prev_i = i - di
                            prev_j = j - dj
                            if prev_i < 0 or prev_j < 0:
                                continue
                            new_dp[i][j] = max(new_dp[i][j], dp[prev_i][prev_j] + value)
            dp = new_dp
        
        return max(dp[n-1][n-1], 0)
