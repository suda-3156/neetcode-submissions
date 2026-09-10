# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = right = head  # inclusive
        dummy = ListNode()  # return dummy.next
        prev_section_last = dummy
        count = 1

        while right:
            # forward `right` by k steps
            while count < k and right:
                right = right.next
                count += 1
            
            if right is None:
                prev_section_last.next = left
                break

            # reverse the section
            next_section_head = right.next
            cur_section_last = left
            # Original: prev_section_last / 1 = left -> 2 -> 3 = right -> next_section_head
            while left != next_section_head:
                next_node = left.next
                left.next = prev_section_last.next
                prev_section_last.next = left
                left = next_node

            # update and reset
            prev_section_last = cur_section_last
            left = right = next_section_head
            count = 1

        return dummy.next
