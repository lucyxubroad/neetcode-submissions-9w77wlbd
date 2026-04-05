# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        q = collections.deque()
        right_side_view = []
        q.append(root)

        while len(q) > 0:
            qLen = len(q)
            for index in range(qLen):
                node = q.popleft()
                if index == 0:
                        right_side_view.append(node.val)
                if node.right is not None:
                    q.append(node.right)
                if node.left is not None:
                    q.append(node.left)
        
        return right_side_view


