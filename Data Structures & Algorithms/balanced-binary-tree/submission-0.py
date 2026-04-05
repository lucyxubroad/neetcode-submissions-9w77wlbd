# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.balanced = True

    def balancedHeights(self, node:TreeNode) -> (bool,int,int):
        if node is None: 
            return (0,0)
        left_inc = 0 if (node.left is None) else 1
        right_inc = 0 if (node.right is None) else 1
        (left_height, right_height) = (max(self.balancedHeights(node.left)) + left_inc, max(self.balancedHeights(node.right)) + right_inc)
        self.balanced =  self.balanced and abs(left_height - right_height) <= 1
        return (left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balancedHeights(root)
        return self.balanced
        