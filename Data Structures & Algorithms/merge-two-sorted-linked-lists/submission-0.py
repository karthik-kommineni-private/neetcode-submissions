# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        head = ListNode()
        curr = head  
        #edgecases - one list is done, list empty,none

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next   
            else:
                curr.next = list2
                list2 = list2.next      
            curr = curr.next

        if not list1:
            curr.next =list2
        if not list2:
            curr=list1    
        return head.next