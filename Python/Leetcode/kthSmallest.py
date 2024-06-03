# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tree_lst = self.getTreeAsList(root)
        return tree_lst[k-1]
    
    def getTreeAsList(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def inorder(node):
            if node is not None:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)
        
        inorder(root)
        return result
