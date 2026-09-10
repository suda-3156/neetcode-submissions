"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        nhead = Node(x=head.val)
        cur = head.next
        ncur = nhead

        while cur:
            ncur.next = Node(x=cur.val)
            cur = cur.next
            ncur = ncur.next

        cur = head
        ncur = nhead
        map = {}  # original -> new
        while cur:
            map[cur] = ncur
            cur = cur.next
            ncur = ncur.next

        cur = head
        ncur = nhead
        while cur:
            ncur.random = map[cur.random] if cur.random else None
            cur = cur.next
            ncur = ncur.next

        return nhead
