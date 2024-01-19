# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        nodeList1 = []
        nodeList2 = []
        self.findLeafDepths(root1, nodeList1)
        self.findLeafDepths(root2, nodeList2)
        return nodeList1 == nodeList2

    def findLeafDepths(self, node, nodeList):
        if not node: return
        if not node.left and not node.right: nodeList.append(node.val)
        else:
            self.findLeafDepths(node.left, nodeList)
            self.findLeafDepths(node.right, nodeList)