# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None

        # [0, n-1, 1, n-2, 2, n-3, 3, ..., n-k+1, k-1, n-k, k] where n = 2m + 1, k = m
        # [0, n-1, 1, n-2, 2, n-3, 3, ..., n-k+1, k-1, n-k (== k)] where n = 2m, k = m

        # length
        n = 1
        cur = head
        while cur.next is not None:
            n += 1
            cur = cur.next

        k = n // 2

        cur = head
        idx = 0
        idxnodes = {}
        while idx <= k:
            idxnodes[idx] = cur
            idx += 1
            cur = cur.next

        idxnodes[k].next = None

        if n % 2 == 0:
            k -= 1

        for i in range(k, 0, -1):
            temp = cur.next if cur else None
            idxnodes[i - 1].next = cur
            cur.next = idxnodes[i]
            cur = temp

        return None
