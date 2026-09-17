# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = deque()
        stack.append([p, q])

        while stack:
            p, q = stack.pop()

            if p is None and q is None:
                continue

            if (not p or not q) or (p.val != q.val):
                return False

            stack.append([p.left, q.left])
            stack.append([p.right, q.right])

        return True