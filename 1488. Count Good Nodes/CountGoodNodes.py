# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
 def goodNodes(self, root: TreeNode) -> int:
    count = 0

    def dfs(node, cMax):
        nonlocal count

        if not node:
            return
        if node.val >= cMax:
            count += 1
            cMax = node.val
        dfs(node.left, cMax)
        dfs(node.right, cMax)
        
    dfs(root, root.val)

    return count
        