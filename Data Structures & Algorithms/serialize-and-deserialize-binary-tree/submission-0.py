# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Codec:
    def __init__(self):
        self.sep = ","
        self.marker = "#"

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        inorder = []
        preorder = []

        def dfs(root: Optional[TreeNode]) -> None:
            if not root:
                return

            preorder.append(root.val)
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)

        dfs(root)

        res = ""
        for n in inorder:
            res += str(n) + self.sep

        res = res[:-1]
        res += self.marker

        for n in preorder:
            res += str(n) + self.sep

        return res[:-1]

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        parts = data.split("#")

        if parts[0] == "":
            return None

        inorder = list(map(int, parts[0].split(",")))
        preorder = list(map(int, parts[1].split(",")))

        indices = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def dfs(l, r):
            nonlocal pre_idx

            if l > r:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root

        return dfs(0, len(inorder) - 1)
