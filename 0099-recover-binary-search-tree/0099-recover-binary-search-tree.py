# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.last = None
        self.first = None
        self.second = None
        self._recoverTree(root)

        self.first.val, self.second.val = self.second.val, self.first.val

        return

    def _recoverTree(self, node):

        if not node: return

        # inorder traverse
        self._recoverTree(node.left)

        if self.last and node.val < self.last.val:
            if not self.first:
                self.first = self.last
            # elif not self.second:     # in some cases, two anomalies can be found and the second anomaly gives the actual node that needs to be swapped.
            #     self.second = node
            self.second = node

        self.last = node

        self._recoverTree(node.right)

        return

# 123456 / 153426