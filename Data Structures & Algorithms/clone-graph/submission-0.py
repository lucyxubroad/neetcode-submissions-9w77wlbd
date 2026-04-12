"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def recurseClone(self, node, cloned_map):
        if node.val in cloned_map:
            return cloned_map[node.val]
        
        clone = Node(node.val)
        cloned_map[node.val] = clone

        for n in node.neighbors:
            cloned_n = self.recurseClone(n, cloned_map)
            clone.neighbors.append(cloned_n)
        
        return clone


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        cloned_map = {}
        return self.recurseClone(node, cloned_map)


        