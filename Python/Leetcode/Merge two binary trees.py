# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        
        merged_tree = TreeNode(
            (root1.val if root1 else 0) 
            + 
            (root2.val if root2 else 0)
        )

        merged_tree.left = self.mergeTrees(
            root1.left if root1 else None,
            root2.left if root2 else None
        )

        merged_tree.right = self.mergeTrees(
            root1.right if root1 else None,
            root2.right if root2 else None
        )

        return merged_tree
