# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def rec(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            
            return max(rec(root.left), rec(root.right)) + 1
        
        return rec(root)