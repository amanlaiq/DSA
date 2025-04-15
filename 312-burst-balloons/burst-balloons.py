from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add boundaries to the array
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[i][j] will represent the maximum coins obtainable by bursting 
        # all balloons in the interval (i, j) (i and j are not burst)
        dp = [[0] * n for _ in range(n)]
        
        # We consider intervals of length 2 or more.
        # Since i and j represent boundaries, the smallest interval we care about is when j-i = 2,
        # which means there's one balloon between i and j.
        for length in range(2, n):
            # i is the left boundary; j = i + length is the right boundary
            for i in range(0, n - length):
                j = i + length
                # k is the index of the balloon burst last in (i, j)
                for k in range(i + 1, j):
                    # When balloon k is burst last, the coins earned will be:
                    #  dp[i][k] (coins from left interval) + 
                    #  dp[k][j] (coins from right interval) + 
                    #  nums[i] * nums[k] * nums[j] (coins from bursting k last)
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        
        # The answer is the maximum coins obtainable by bursting all balloons in (0, n-1),
        # which means using all balloons in the original array.
        return dp[0][n - 1]
