from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        """
        Calculate the triangular sum of a list of integers.
        The triangular sum of a list of integers is obtained by the following process:
        - Replace each element by the sum of itself and the next element, modulo 10.
        - Repeat the process until only one number remains.
      
        Args:
        nums (List[int]): A list of integers between 0 and 9 inclusive.
      
        Returns:
        int: The final integer (between 0 to 9) after the process is done.
        """
        # Get the initial length of nums
        n = len(nums)
      
        # Loop from the length of nums down to 1
        for i in range(n, 0, -1):
            # Calculate the new values for the triangular sum step
            for j in range(i - 1):
                # Update each element with the sum of itself and the next element, mod 10
                nums[j] = (nums[j] + nums[j + 1]) % 10
      
        # The first element of the list is the answer after the process
        return nums[0]

# Note: The method name has been changed to 'triangular_sum' to match the Python naming convention.
# All variable names are already properly named, and no method names have been altered.
