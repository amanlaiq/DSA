class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [0] + [inf] * n

        for c, t in zip(cost, time):
            for j in range(n, 0, -1):
                dp[j] = min(dp[j], dp[max(j - (t + 1), 0)] + c)
        return dp[n]

# class Solution:
#     def paintWalls(self, cost: List[int], time: List[int]) -> int:
#         n = len(cost)
#         dp = [0] + [inf] * n
#         for c, t in zip(cost, time):
#             for j in range(n, 0, -1):
#                 dp[j] = min(dp[j], dp[max(j - (t + 1), 0)] + c) #the question I am asking here is, can I paint j walls by choosing this particular wall ie t + 1
#         return dp[n]
    