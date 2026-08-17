from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Handle empty graph
        if node is None:
            return None

        # Map original node -> cloned node
        old_to_new = {}

        # BFS traversal
        queue = deque([node])
        old_to_new[node] = Node(node.val)

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                # Clone neighbor on first visit
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Always connect clone -> clone
                old_to_new[curr].neighbors.append(old_to_new[neighbor])

        # Return cloned entry node
        return old_to_new[node]
