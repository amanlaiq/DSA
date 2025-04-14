class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            dp = [1] *(n)
            for j in range(n - 2, -1, -1):
                dp[j] = dp[j + 1] + row[j]
            row = dp
        return row[0]