"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldPointerToNode = {None:None}
        curr = head
        while curr:
            oldPointerToNode[curr] = Node(curr.val)
            curr = curr.next

        newCurr = head
        while newCurr:
            newCopyNode = oldPointerToNode[newCurr]
            newCopyNode.next = oldPointerToNode[newCurr.next]
            newCopyNode.random = oldPointerToNode[newCurr.random]
            newCurr = newCurr.next

        return oldPointerToNode[head]    
        