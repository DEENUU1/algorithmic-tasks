# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root is None:
            return False
        if self.isSameTree(root, subRoot):
            return True  

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, node1, node2) -> bool:
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False

        return (
            node1.val == node2.val
            and self.isSameTree(node1.left, node2.left)
            and self.isSameTree(node1.right, node2.right)
        )
