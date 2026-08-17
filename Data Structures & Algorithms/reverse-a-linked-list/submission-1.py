from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ─── Base cases ───────────────────────────────────────────────
        # Empty list or single-node list: nothing to reverse
        if head is None or head.next is None:
            return head

        # ─── Iterative reversal ─────────────────────────────────────
        prev = None
        curr = head

        while curr:
            # 1) Detach curr from the rest
            nxt = curr.next
            # 2) Reverse the pointer
            curr.next = prev
            # 3) Advance both pointers
            prev = curr
            curr = nxt

        # prev is the new head
        return prev
