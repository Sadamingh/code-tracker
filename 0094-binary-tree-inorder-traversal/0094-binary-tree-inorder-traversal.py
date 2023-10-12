# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self._inorderTraversal(root, [])

    def _inorderTraversal(self, node, travList):
        if not node: return travList

        self._inorderTraversal(node.left, travList) if node.left else None
        travList.append(node.val)
        self._inorderTraversal(node.right, travList) if node.right else None

        return travList