# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        queue = [root]
        level = 1
        max_level = 1
        max_sum = root.val

        while queue:
            level_sum = 0
            level_size = len(queue)

            for i in range(level_size):
                cur_node = queue.pop(0)
                level_sum += cur_node.val

                if cur_node.left:
                    queue.append(cur_node.left)

                if cur_node.right:
                    queue.append(cur_node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            level += 1

        return max_level