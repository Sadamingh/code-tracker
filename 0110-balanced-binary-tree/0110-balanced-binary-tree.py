# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.maxDepth(root) == -1:
            return False
        return True

    def maxDepth(self, node):
        if not node: return 0

        leftDepth = self.maxDepth(node.left)
        rightDepth = self.maxDepth(node.right)

        if leftDepth == -1 or rightDepth == -1:
            return -1

        if abs(leftDepth - rightDepth) > 1:
            return -1

        return max(leftDepth, rightDepth) + 1


    #     if not root:
    #         return True

    #     depList = self.getDepths(root, [])
    #     # print(depList)

    #     if max(depList) - min(depList) > 1:
    #         return False
    #     else:
    #         return True

    # def getDepths(self, node, depList, count=1):

    #     if not node: return depList
    #     if node.left:
    #         self.getDepths(node.left, depList, count+1)
    #     if node.right:
    #         self.getDepths(node.right, depList, count+1)
    #     if not node.left or not node.right: 
    #         depList.append(count)

    #     return depList