# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.k_element = None

    def dfs(self, node, k):
        if node is None: 
            return []
        elements = (self.dfs(node.left, k) + [node.val] + self.dfs(node.right, k))
        if len(elements) >= k:
            self.k_element = elements[k-1]
        return elements
             
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root, k)
        return self.k_element
        