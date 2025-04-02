# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, List1: Optional[ListNode], List2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while List1 and List2:
            if List1.val < List2.val:
                node.next = List1
                List1 = List1.next
            else:
                node.next = List2
                List2 = List2.next
            node = node.next
        node.next = List1 or List2
        return dummy.next