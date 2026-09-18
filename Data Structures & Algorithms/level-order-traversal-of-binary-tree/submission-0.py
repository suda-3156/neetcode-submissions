# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        leveled_nodes = defaultdict(list)
        level = 0

        while queue:
            length = len(queue)
            level += 1

            for _ in range(length):
                cur = queue.popleft()
                leveled_nodes[level].append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return list(leveled_nodes.values())
