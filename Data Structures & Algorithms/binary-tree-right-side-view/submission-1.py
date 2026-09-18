# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        result = []
        queue.append(root)

        if root is None:
            return []

        while queue:
            cur_len = len(queue)

            for i in range(cur_len):
                cur = queue.popleft()

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

                if i == cur_len - 1:
                    result.append(cur.val)

        return result
