"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None
        otn_map = {} #{oldNode: NewNode} 
        q = deque()
        q.append(node)
        otn_map[node] = Node(node.val)

        #iterate old nodes
        while q:
            for i in range(len(q)):
                curr_node = q.popleft()
                curr_node_neighbors = curr_node.neighbors

                for i in range(len(curr_node_neighbors)):
                    neighbor = curr_node_neighbors[i]
                    if neighbor not in otn_map:
                            otn_map[neighbor] = Node(neighbor.val) 
                            q.append(neighbor)

                    otn_map[curr_node].neighbors.append(otn_map[neighbor])
                                 
        return  otn_map[node]  
        