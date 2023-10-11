# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        treeP = self.traverse(p, [])
        treeQ = self.traverse(q, [])
        if len(treeP) != len(treeQ):
            return False
        else:
            for i in range(len(treeP)):
                if treeP[i] != treeQ[i]:
                    return False
        return True

    def traverse(self, node, treeList):
        if not node: return treeList
        treeList.append(node.val)
        self.traverse(node.left, treeList) if node.left else treeList.append(None)
        self.traverse(node.right, treeList) if node.right else treeList.append(None)
        return treeList