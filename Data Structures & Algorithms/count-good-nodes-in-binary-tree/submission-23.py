# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
                
        def dfs(node, maxVal):
            if not node:
                return 0
            
            good = 0
            if node.val >= maxVal:
                maxVal = node.val
                good = 1

            left = dfs(node.left, maxVal)
            right = dfs(node.right, maxVal)

            return left + right + good
        
        return dfs(root, float('-inf'))