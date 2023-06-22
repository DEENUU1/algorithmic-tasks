# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        sub = targetSum - root.val

        if sub == 0 and root.left is None and root.right is None:
            return True

        if root.left is not None and self.hasPathSum(root.left, sub):
            return True
        if root.right is not None and self.hasPathSum(root.right, sub):
            return True
        
        return False