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
            #break ties
            nextNode = curr.next
            curr.next = prev
            #move
            prev = curr
            curr = nextNode
        
        return prev    
            

    def mergeList(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            temp1 = list1.next
            temp2 = list2.next
            curr.next = list1
            curr = curr.next
            curr.next = list2
            curr = curr.next
            list1 = temp1
            list2 = temp2

        curr.next = list1 or list2    
            
        return dummy.next    




        