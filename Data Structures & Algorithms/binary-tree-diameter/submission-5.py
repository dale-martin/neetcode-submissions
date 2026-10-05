# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.maxLen(root)[1]
        
    def maxLen(self, root):
        if not root:
            return (0, 0)
        
        lDepth, lMaxLen = self.maxLen(root.left)
        rDepth, rMaxLen = self.maxLen(root.right)

        depth = max(lDepth, rDepth) + 1
        maxLen = max(lDepth + rDepth, lMaxLen, rMaxLen)

        return (depth, maxLen)