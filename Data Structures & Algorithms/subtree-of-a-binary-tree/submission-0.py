# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = deque()
        stack.append(root)

        while stack:
            cur = stack.pop()

            if self.isSame(cur, subRoot):
                return True
            elif cur is not None:
                stack.append(cur.left)
                stack.append(cur.right)

        return False

    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def rec(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True

            if (not p or not q) or (p.val != q.val):
                return False

            return rec(p.left, q.left) and rec(p.right, q.right)

        return rec(p, q)