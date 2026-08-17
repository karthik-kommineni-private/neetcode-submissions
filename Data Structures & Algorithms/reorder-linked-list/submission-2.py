# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head

        middle = self.getMiddle(head)

        list2 = self.getReverse(middle.next)
        middle.next = None
        list1 = head
        self.mergeList(list1,list2)

    def getMiddle(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        return slow

    def getReverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode 
        return prev    
            

    def mergeList(self, list1: ListNode, list2: ListNode) -> ListNode:
        while list2:
            temp1, temp2 = list1.next,list2.next
            list1.next = list2
            list2.next = temp1
            list1, list2= temp1, temp2
              
