"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cc = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            cc[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = cc[cur]
            copy.next = cc[cur.next]
            copy.random = cc[cur.random]
            cur = cur.next

        return cc[head]