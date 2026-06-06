class Node:
    def __init__(self, num):
        self.num = num
        self.neighbors = []

    def addNeighbor(self, node):
        self.neighbors.append(node)

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes_dictionary = {i: Node(i) for i in range(n)}

        for (edge_start, edge_end) in edges:
            start_node, end_node = nodes_dictionary[edge_start], nodes_dictionary[edge_end]
            start_node.addNeighbor(end_node)
            end_node.addNeighbor(start_node)

        visited_set = set()

        traversal = [(nodes_dictionary[0], -1, set())]
        while len(traversal) > 0:
            (node, parent, path) = traversal.pop(0)
            # print(node.num, parent, path)
            visited_set.add(node.num)
            if node.num in path:
                return False
            path_copy = path.copy()
            path_copy.add(node.num)
            for neighbor in node.neighbors:
                if neighbor.num != parent:
                    traversal.append((neighbor, node.num, path_copy))

        # print(len(visited_set), n, len(visited_set) == n)
        return len(visited_set) == n

        