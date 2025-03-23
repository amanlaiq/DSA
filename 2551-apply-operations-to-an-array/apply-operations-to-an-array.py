class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        length = len(nums)

        for i in range(length - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        result = [0] * length

        result_index = 0

        for num in nums:
            if num:
                result[result_index] = num
                result_index += 1
        return result