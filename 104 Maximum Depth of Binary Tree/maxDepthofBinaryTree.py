# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depthSearch(root, depth):
            if not root: return depth
            return max(depthSearch(root.left, depth + 1), depthSearch(root.right, depth + 1))

        return depthSearch(root,0)
        