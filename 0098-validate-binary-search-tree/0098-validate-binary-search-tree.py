# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBST(root, -inf, inf)

    def _isValidBST(self, node, low, high):

        if not node: return True

        if node.val <= low or node.val >= high:
            return False

        return self._isValidBST(node.left, low, node.val) and self._isValidBST(node.right, node.val, high)
        
        # if not root: return True

        # if root.left and root.left.val >= root.val:
        #     return False
        # if root.right and root.right.val <= root.val:
        #     return False

        # return self.isValidBST(root.left) and self.isValidBST(root.right)
        
