class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cursum = 0 
        prefix = { 0 : 1 }

        for n in nums:
            cursum += n
            diff = cursum - k

            res += prefix.get(diff, 0)
            prefix[cursum] = 1 + prefix.get(cursum, 0)

        return res