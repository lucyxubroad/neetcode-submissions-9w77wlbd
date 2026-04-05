# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.traversal = []

    def search(self, node, layer):
        if node is None:
            return
        if len(self.traversal) < layer:
            new_layer = [node.val]
            self.traversal.append(new_layer)
        else:
            self.traversal[layer-1].append(node.val)
        self.search(node.left, layer+1)
        self.search(node.right, layer+1)        

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.search(root, 1)
        return self.traversal
        