# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return None

            if depth == len(res):
                res.append(node.val)

            # right mostから処理するので、res.appendはright most nodeに対して行われる
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res