# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def rec(root: Optional[TreeNode]) -> int:
            nonlocal balanced
            
            if root is None:
                return 0

            left = rec(root.left)
            right = rec(root.right)

            if abs(left - right) > 1:
                balanced = False

            return max(left, right) + 1

        rec(root)
        return balanced
