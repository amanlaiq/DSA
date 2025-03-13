class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False] * len(nums)

        def backtrack(i, k, subsetsum):
            if k == 0:
                return True
            if subsetsum == target:
                return backtrack(0, k - 1, 0)
            
            for j in range(i, len(nums)):
                if used[j] or subsetsum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j + 1, k, subsetsum + nums[j]):
                    return True
                used[j] = False

                if subsetsum == 0:
                    break
            return False
        return backtrack(0, k, 0)

