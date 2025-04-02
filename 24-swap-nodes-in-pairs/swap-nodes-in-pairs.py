# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:  # Base case
            return head
        
        temp = head.next  # Store the second node
        head.next = self.swapPairs(temp.next)  # Recursively swap the rest of the list
        temp.next = head  # Swap current pair
        
        return temp  # New head of the swapped pair
        