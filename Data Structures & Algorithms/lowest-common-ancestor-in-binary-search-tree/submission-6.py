# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = None

        def dfs(node):
            nonlocal lca

            if not node:
                return (False, False)

            left = dfs(node.left)
            right = dfs(node.right)

            pFound = node == p or left[0] or right[0]
            qFound = node == q or left[1] or right[1]

            if not lca and pFound and qFound:
                lca = node
            
            return (pFound, qFound)

        dfs(root)
        return lca
