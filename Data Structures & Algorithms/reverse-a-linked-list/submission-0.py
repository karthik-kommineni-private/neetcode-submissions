# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #edge cases - head -empty, one node only
        if head is None or head.next is None:
            return head

        #notes -imag 2 nodes - dummy/no ?
        dummyNode = None
        prev = dummyNode
        curr = head

        while curr:
            #change conections
            tempNode = curr.next
            curr.next = prev
            #move forward
            prev = curr
            curr = tempNode

        return prev

