# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent_val):
            if not node:
                return 0

            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)
            self.res = max(self.res, left + right)

            if node.val == parent_val:
                return 1 + max(left, right)
            else:
                return 0

        self.res = 0
        dfs(root, None)
        return self.res