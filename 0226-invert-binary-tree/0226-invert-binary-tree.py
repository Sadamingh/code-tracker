# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self._invertTree(root)

    def _invertTree(self, node):
        if not node: return node

        self._invertTree(node.left) if node.left else None
        self._invertTree(node.right) if node.right else None

        if node.left or node.right:
            node.left, node.right = node.right, node.left

        return node