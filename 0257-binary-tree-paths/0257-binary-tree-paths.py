# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.getPaths(root, "", [])

    def getPaths(self, node, path, pathList):

        if not node: return pathList

        if node.left or node.right:
            path += str(node.val) + "->"

        self.getPaths(node.left, path, pathList) if node.left else None
        self.getPaths(node.right, path, pathList) if node.right else None

        if not node.left and not node.right:
            path += str(node.val)
            pathList.append(path)

        return pathList
