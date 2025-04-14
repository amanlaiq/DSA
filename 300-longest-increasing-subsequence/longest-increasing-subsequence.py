class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
        return max(lis)



# from typing import List
# from functools import lru_cache

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         lis = []

#         for i in nums:
#             indx = bisect.bisect_left(lis, i)
#             if indx == len(lis):
#                 lis.append(i)
#             else:
#                 lis[indx] = i

            
#         return len(lis)