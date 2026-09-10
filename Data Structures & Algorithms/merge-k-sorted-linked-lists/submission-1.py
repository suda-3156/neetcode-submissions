# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # sort list
        for i in range(len(lists) - 1, -1, -1):
            if not lists[i]:
                del lists[i]

        lists.sort(key=lambda node: node.val)

        dummy = ListNode()
        cur = dummy
        while lists:
            cur.next = lists.pop(0)
            nxt = cur.next.next
            if nxt is not None:
                self.insert(lists, nxt)

            cur = cur.next
            cur.next = None

        return dummy.next

    def insert(self, lists: List[Optional[ListNode]], nxt: Node) -> None:
        left, right = 0, len(lists)

        while left < right:
            mid = (left + right) // 2

            if lists[mid].val >= nxt.val:
                right = mid
            else:
                left = mid + 1

        lists.insert(left, nxt)
