# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        min_level, max_level = float('infinity'), - float('infinity')

        # DFS
        stack = deque()
        stack.append([root, 1])

        while stack:
            cur, lvl = stack.pop()

            if cur.right:
                stack.append([cur.right, lvl + 1])
            if cur.left:
                stack.append([cur.left, lvl + 1])

            if not cur.right and not cur.left:
                min_level = min(min_level, lvl)
                max_level = max(max_level, lvl)

        return abs(max_level - min_level) <= 1
