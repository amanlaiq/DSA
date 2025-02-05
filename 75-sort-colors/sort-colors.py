# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         count = [0] * 3

#         for num in nums:
#             count[num] += 1

#         index = 0
#         for i in range(3):
#             while count[i]:
#                 count[i] -= 1
#                 nums[index] = i
#                 index += 1

#         return num


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Step 1: Find the minimum and maximum values in the array
        min_val = min(nums)
        max_val = max(nums)

        # Step 2: Create a count array for all numbers in the range [min_val, max_val]
        count = [0] * (max_val - min_val + 1)

        # Step 3: Count the occurrences of each number in the array
        for num in nums:
            count[num - min_val] += 1  # Use num - min_val to map number to index

        # Step 4: Rebuild the sorted array
        index = 0
        for i in range(len(count)):
            while count[i] > 0:
                nums[index] = i + min_val  # Convert index back to actual number
                index += 1
                count[i] -= 1
