# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootSerial = self.serialise(root)
        subRootSerial = self.serialise(subRoot)
        combined = subRootSerial + '&' + rootSerial

        z = self.z_function(combined)
        subRootLen = len(subRootSerial)

        for i in range(subRootLen + 1, len(combined)):
            if z[i] == subRootLen:
                return True
        
        return False
    
    def serialise(self, root):
        res = []

        def dfs(node):
            if node is None:
                res.append('|#')
                return
            
            res.append('|')
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ''.join(res)
    
    def z_function(self, s: str) -> list:
        z = [0] * len(s)
        l, r, n = 0, 0, len(s)
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        return z
