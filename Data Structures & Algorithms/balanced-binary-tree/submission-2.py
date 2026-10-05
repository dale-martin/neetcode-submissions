# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]
    
    def dfs(self, root):
        if not root:
            return (True, 0)

        lBal, lDepth = self.dfs(root.left)
        rBal, rDepth = self.dfs(root.right)

        bal = abs(lDepth - rDepth) <= 1
        
        if not lBal or not rBal or not bal:
            return (False, 0)

        return (True, max(lDepth, rDepth) + 1)