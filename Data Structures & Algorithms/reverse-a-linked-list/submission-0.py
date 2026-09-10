# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        dummy = ListNode(next=ListNode(val=head.val))
        cur = head.next

        while cur is not None:
            temp = cur.next

            dummy.next = ListNode(val=cur.val, next=dummy.next)

            cur = temp

        return dummy.next