# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        dummy = ListNode()
        ans = dummy

        carry = 0
        while cur1 or cur2 or carry:
            val = carry
            carry = 0

            if cur1:
                val += cur1.val
                cur1 = cur1.next
            if cur2:
                val += cur2.val
                cur2 = cur2.next

            carry = val // 10
            val = val - carry * 10

            ans.next = ListNode(val)
            ans = ans.next

        return dummy.next
