# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        treeP = self.leftTraverse(root.left, [])
        treeQ = self.rightTraverse(root.right, [])
        if len(treeP) != len(treeQ):
            return False
        else:
            for i in range(len(treeP)):
                if treeP[i] != treeQ[i]:
                    return False
        return True

    def leftTraverse(self, node, treeList):
        if not node: return treeList
        treeList.append(node.val)
        self.leftTraverse(node.left, treeList) if node.left else treeList.append(None)
        self.leftTraverse(node.right, treeList) if node.right else treeList.append(None)
        return treeList

    def rightTraverse(self, node, treeList):
        if not node: return treeList
        treeList.append(node.val)
        self.rightTraverse(node.right, treeList) if node.right else treeList.append(None)
        self.rightTraverse(node.left, treeList) if node.left else treeList.append(None)
        return treeList