class Node:
    def __init__(self, num):
        self.num = num
        self.neighbors = []

    def addNeighbor(self, node):
        self.neighbors.append(node)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes_dictionary = {i: Node(i) for i in range(n)}

        for (edge_start, edge_end) in edges:
            start_node, end_node = nodes_dictionary[edge_start], nodes_dictionary[edge_end]
            start_node.addNeighbor(end_node)
            end_node.addNeighbor(start_node)


        num_components = 0
        all_visited = set()

        for node_num in range(n):
            if node_num not in all_visited:
                to_traverse = [(nodes_dictionary[node_num], set())]
                while len(to_traverse) > 0:
                    (visit_node, visited_path) = to_traverse.pop(0)
                    visited_path.add(visit_node.num)
                    all_visited.add(visit_node.num)
                    for neighbor in visit_node.neighbors:
                        if neighbor.num not in visited_path:
                            to_traverse.append((neighbor, visited_path))
                num_components+=1

        return num_components