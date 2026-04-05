# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.d = 0

    def max_tuple(self, tup: (int,int)) -> int:
        (x,y) = tup
        return max(x,y)

    def diameter(self, node: Optional[TreeNode]) -> (int, int):
        if node is None:
            return (0, 0)
        (left_inc, right_inc) = (0,0)
        if node.left is not None:
            left_inc = 1
        if node.right is not None:
            right_inc = 1
        (left_height, right_height) = (
            left_inc + self.max_tuple(self.diameter(node.left)), 
            right_inc + self.max_tuple(self.diameter(node.right))
        )
        self.d = max(self.d,left_height+right_height)
        return (left_height, right_height)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter(root)
        return self.d
        