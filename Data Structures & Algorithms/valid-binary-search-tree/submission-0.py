# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) -> List[float]: # max, min, validity
            if root is None:
                return [-float('infinity'), float('infinity'), 1]

            left_max, left_min, left_valid = dfs(root.left)
            right_max, right_min, right_valid = dfs(root.right)

            if left_max < root.val < right_min and left_valid and right_valid:
                return [max(left_max, root.val, right_max), min(left_min, root.val, right_min), 1]
            else:
                return [-float('infinity'), float('infinity'), 0]

        _, _, valid = dfs(root)
        return valid == 1
