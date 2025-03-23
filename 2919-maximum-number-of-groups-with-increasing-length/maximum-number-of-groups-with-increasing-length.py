class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        total = k = 0
        for a in usageLimits:
            total += a
            if total >= (k + 1) * (k + 2) // 2:
                k += 1
        return k