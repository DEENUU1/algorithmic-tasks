# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = [(root, float('-inf'))]
        c = 0

        while stack:
            node, max_num = stack.pop()
            if node.val >= max_num:
                c += 1
            max_num = max(max_num, node.val)
            if node.left:
                stack.append((node.left, max_num))
            if node.right:
                stack.append((node.right, max_num))

        return c
