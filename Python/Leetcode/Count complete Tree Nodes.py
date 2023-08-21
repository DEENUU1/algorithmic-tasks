# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def inorder_traversal(node, values):
            if node:
                inorder_traversal(node.left, values)
                values.append(node.val)
                inorder_traversal(node.right, values)

        root_values = []
        inorder_traversal(root, root_values)
        
        total = 0
        for i in root_values:
            total += 1

        return total 