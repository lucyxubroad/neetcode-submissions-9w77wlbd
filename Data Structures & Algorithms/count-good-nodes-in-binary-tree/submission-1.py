# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# look at each layer. 
# if at your layer, you are > than the max at all previous layers, increment.  

class Solution:
    def __init__(self):
        self.num_good_nodes = 0

    def dfs(self,node, max_in_path):
        if node.val >= max_in_path:
            self.num_good_nodes += 1
            max_in_path = node.val
        if node.left is not None:
            self.dfs(node.left, max_in_path)
        if node.right is not None:
            self.dfs(node.right, max_in_path)
    
    def goodNodes(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        self.dfs(root, root.val)

        return self.num_good_nodes

            