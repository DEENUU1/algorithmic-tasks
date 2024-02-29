# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        self.dfs(res, root)
        return res[0]
        
    def dfs(self, res, root):
        if not root:
            return 0
        
        left = self.dfs(res, root.left)
        right = self.dfs(res, root.right)
        res[0] = max(res[0], left + right)

        return 1 + max(left, right)
