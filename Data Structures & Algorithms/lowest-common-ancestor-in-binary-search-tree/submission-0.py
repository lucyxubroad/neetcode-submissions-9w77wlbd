# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.found_nodes = 0
        self.node_to_ancestors = {}

    def search(self, node, p, q, path):
        if node is None: 
            return
        if self.found_nodes == 2:
            return
        node_path = path.copy()
        node_path.insert(0,node)
        self.node_to_ancestors[node.val] = node_path
        if node.val == p.val or node.val == q.val:
            self.found_nodes+=1
        self.search(node.left, p, q, node_path)
        self.search(node.right, p, q, node_path)


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.search(root, p, q, [])
        p_path = self.node_to_ancestors[p.val]
        q_path = self.node_to_ancestors[q.val]
        for p_ancestor in p_path:
            for q_ancestor in q_path:
                if p_ancestor.val == q_ancestor.val:
                    return p_ancestor
        

            