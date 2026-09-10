# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        map: dict[int, ListNode] = {}
        length = 0
        cur = head

        while cur:
            map[length] = cur
            length += 1
            cur = cur.next

        if n == length:
            return head.next

        if n == 1:
            map[length - 2].next = None
        else:
            map[length - n - 1].next = map[length - n + 1]
        return head
