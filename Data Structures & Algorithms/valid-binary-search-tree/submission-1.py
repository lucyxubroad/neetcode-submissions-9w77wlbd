# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, node, minimum, maximum):
        if node is None:
            return True
        if node.val <= minimum or node.val >= maximum:
            return False
        return self.dfs(node.left, minimum,node.val) and self.dfs(node.right,node.val, maximum)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -math.inf, math.inf)