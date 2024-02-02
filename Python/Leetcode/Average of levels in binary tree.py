# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if root is None:
            return 0
        
        queue = [root]
        level = 1
        max_level = 1
        res = []

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
            
            avg = level_sum / level_size
            res.append(avg)

        return res
