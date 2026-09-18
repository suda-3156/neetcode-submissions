# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root: TreeNode, max_val: float) -> None:
            nonlocal res
            
            if root.val >= max_val:
                res += 1

            max_val = max(max_val, root.val)
            if root.right:
                dfs(root.right, max_val)
            if root.left:
                dfs(root.left, max_val)

        dfs(root, -float("infinity"))
        return res
