# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}

        pre_idx = 0

        def rec(l: int, r: int) -> Optional[TreeNode]:
            nonlocal pre_idx

            if l > r:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1
            in_idx = indices[root_val]

            root = TreeNode(root_val)

            root.left = rec(l, in_idx - 1)
            root.right = rec(in_idx + 1, r)

            return root

        return rec(0, len(preorder) - 1)
