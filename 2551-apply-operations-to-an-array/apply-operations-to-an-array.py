from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Get the length of the list 'nums'.
        length = len(nums)

        # Iterate over the list elements, except for the last element.
        for i in range(length - 1):
            # If the current element is the same as the next element,
            # double its value and set the next element to 0.
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
      
        # Create a new list 'result' with the same size filled with zeros.
        result = [0] * length
      
        # Initialize a pointer for the index of 'result'.
        result_index = 0
      
        # Iterate over 'nums' to populate non-zero elements in the 'result'.
        for num in nums:
            # If the element is non-zero, put it in the next position of 'result'.
            if num:
                result[result_index] = num
                result_index += 1
      
        # Return the 'result' list containing the processed numbers.
        return result