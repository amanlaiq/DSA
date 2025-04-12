class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize left and right pointers for binary search
        l, r = 0, len(nums) - 1
        
        # Start with the first element as the initial candidate for minimum
        # This ensures we have a valid starting point to compare against
        res = nums[0]

        # Continue binary search while the left pointer hasn't crossed the right
        while l <= r:
            # If the current range [l, r] is sorted (left < right)
            # Update res with the leftmost element (smallest in this sorted segment)
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                # Note: We could break here since this segment's min is found,
                # but the code continues to ensure correctness

            # Calculate the middle index of the current range
            m = (l + r) // 2
            
            # Update res with the minimum of its current value and the middle element
            # This ensures we track the smallest value seen, as m might be the pivot
            res = min(res, nums[m])
            
            # If middle element is greater than or equal to the left element
            # The left half [l, m] is sorted, so the rotation (and minimum) is in the right half
            if nums[m] >= nums[l]:
                l = m + 1  # Move left pointer past the middle to search the unsorted part
            # If middle element is less than the left element
            # The rotation (and minimum) is in the left half [l, m], before or at m
            else:
                r = m - 1  # Move right pointer before the middle to search the unsorted part

        # Return the smallest value found
        # res will hold the minimum after exploring all necessary segments
        return res